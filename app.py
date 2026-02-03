# app.py

import gradio as gr
import json
import os
from src.intent_parser import parse_intent
from src.menu_data import MENU

# --- HELPER FUNCTIONS ---

def flatten_menu_for_display():
    """Formats menu for the UI Accordion."""
    display_text = ""
    for category, items in MENU.items():
        display_text += f"\n### {category}\n"
        for item in items:
            tags = ", ".join(item['tags'])
            display_text += f"- **{item['name']}** (₹{item['price']}): {item['description']} _[{tags}]_\n"
    return display_text

def format_chef_ticket(json_ticket):
    """Converts the JSON output into a nice HTML/Markdown ticket for the Chef."""
    if not json_ticket:
        return "No Data"
        
    items_html = "<ul>"
    for item in json_ticket.get('ordered_items', []):
        items_html += f"<li><b>{item['quantity']}x {item['name']}</b><br><i>Note: {item.get('notes', '-')}</i></li>"
    items_html += "</ul>"
    
    constraints = ", ".join(json_ticket.get('dietary_constraints', []))
    
    tp = json_ticket.get('taste_profile', {})
    taste_html = f"""
    <b>Spice:</b> {tp.get('spice_level')}<br>
    <b>Oil:</b> {tp.get('oil_level')}<br>
    <b>Salt:</b> {tp.get('salt_level')}<br>
    """
    
    alert_style = "background-color: #ffebee; border: 1px solid red; padding: 10px;" if json_ticket.get('confirm_with_customer') else ""
    conflict_style = "background-color: #fff3cd; border: 1px solid orange; padding: 10px;" if json_ticket.get('conflict_flag') else ""
    
    html = f"""
    <div style="font-family: monospace; border: 2px solid #333; padding: 20px; max-width: 400px;">
        <h2 style="text-align: center; border-bottom: 2px dashed #333;">KITCHEN TICKET</h2>
        <h3>ITEMS</h3>
        {items_html}
        <hr>
        <h3>DIET & PREFERENCES</h3>
        <p><b>Constraints:</b> {constraints or 'None'}</p>
        <p>{taste_html}</p>
        <hr>
        <h3>COOKING NOTES</h3>
        <p>{json_ticket.get('cooking_notes', '-')}</p>
    </div>
    """
    
    if json_ticket.get('conflict_flag'):
        html += f"<div style='{conflict_style}'><b>⚠️ CONFLICT DETECTED:</b> {json_ticket.get('conflict_message')}</div>"
        
    if json_ticket.get('confirm_with_customer'):
        html += f"<div style='{alert_style}'><b>🛑 WAIT! CONFIRM WITH CUSTOMER:</b><br>{json_ticket.get('clarification_question')}</div>"
        
    return html

# --- MAIN LOGIC ---

def process_order(
    api_key, model_name, user_text, 
    spice_slider, oil_radio, sweet_slider, salt_radio, 
    diet_radio, allergy_check, onion_garlic
):
    """Callback for the 'Send Order' button."""
    
    # 1. API Key Check
    real_key = api_key or os.environ.get("GROQ_API_KEY")
    if not real_key:
        return {
            "error": "No API Key provided. Please enter one in the UI or set GROQ_API_KEY."
        }, "<h3>⚠️ Error: Missing API Key</h3>"

    # 2. Structure Inputs
    structured_inputs = {
        "spice": spice_slider,
        "oil": oil_radio,
        "sweetness": sweet_slider,
        "salt": salt_radio,
        "diet": diet_radio,
        "allergies": allergy_check,
        "no_onion_garlic": not onion_garlic # Toggle logic: True = Allowed, False = No onion/garlic
    }
    
    # 3. Call Logic
    # We invert the onion/garlic toggle naming for clarity in logic (UI says "Include?", logic wants constraints)
    if not onion_garlic:
        structured_inputs["dietary_constraints_extra"] = ["No Onion/Garlic"]

    result_json = parse_intent(user_text, structured_inputs, real_key, model_name)
    
    # 4. Format Output
    ticket_html = format_chef_ticket(result_json)
    
    return result_json, ticket_html


# --- UI LAYOUT ---

with gr.Blocks(title="AI Waiter Prototype", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🍛 AI Waiter: Intent → Chef Instructions")
    
    with gr.Row():
        
        # === LEFT COLUMN: CUSTOMER ===
        with gr.Column(scale=1):
            gr.Markdown("### 1. Setup & Menu")
            api_key_input = gr.Textbox(
                label="Groq API Key (Optional if env var set)", 
                type="password",
                placeholder="gsk_..."
            )
            model_selector = gr.Dropdown(
                label="Model", 
                choices=["llama3-70b-8192", "mixtral-8x7b-32768", "llama3-8b-8192"], 
                value="llama3-70b-8192"
            )
            
            with gr.Accordion("📖 View Menu", open=False):
                gr.Markdown(flatten_menu_for_display())
            
            gr.Markdown("### 2. Customize Preferencs")
            with gr.Group():
                with gr.Row():
                    spice_slider = gr.Slider(0, 5, value=2, step=1, label="Spice Level")
                    sweet_slider = gr.Slider(0, 5, value=1, step=1, label="Sweetness")
                
                with gr.Row():
                    oil_radio = gr.Radio(["Low", "Medium", "High"], value="Medium", label="Oil")
                    salt_radio = gr.Radio(["Low", "Normal", "High"], value="Normal", label="Salt")
                
                diet_radio = gr.Radio(
                    ["None", "Vegetarian", "Vegan", "Jain", "Eggetarian", "Non-Veg"], 
                    value="None", 
                    label="Diet Type"
                )
                
                allergy_check = gr.CheckboxGroup(
                    ["Nuts", "Dairy", "Gluten", "Soy", "Shellfish"], 
                    label="Allergies"
                )
                
                onion_garlic = gr.Checkbox(value=True, label="Include Onion & Garlic?")
            
            gr.Markdown("### 3. Order")
            user_text_input = gr.Textbox(
                lines=3, 
                placeholder="e.g., I'd like a Butter Chicken and 2 Naans, but make the chicken extra spicy.", 
                label="Tell us what you want to eat..."
            )
            
            send_btn = gr.Button("👨‍🍳 Send to Chef", variant="primary", size="lg")

        # === RIGHT COLUMN: CHEF ===
        with gr.Column(scale=1):
            gr.Markdown("### 👨‍🍳 Chef View (Instruction Set)")
            
            chef_ticket_display = gr.HTML(label="Visual Ticket")
            
            with gr.Accordion("🔍 Debug / Raw JSON", open=True):
                json_output = gr.JSON(label="Structured Intent Output")

    # --- EVENTS ---
    send_btn.click(
        fn=process_order,
        inputs=[
            api_key_input, model_selector, user_text_input,
            spice_slider, oil_radio, sweet_slider, salt_radio,
            diet_radio, allergy_check, onion_garlic
        ],
        outputs=[json_output, chef_ticket_display]
    )

if __name__ == "__main__":
    demo.launch()
