# src/intent_parser.py

import json
import logging
from src.menu_data import MENU, get_all_items_flat
from src.intent_schema import INTENT_SCHEMA, validate_json
from src.llm_client import call_groq_api

# Basic logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_system_prompt():
    """Generates the system prompt with menu context and schema enforcement."""
    
    # Flatten menu for prompt context
    # In a real app with huge menu, we would use RAG or just send relevant categories.
    # For this prototype, we send the whole menu structure to ensure high accuracy.
    menu_str = json.dumps(MENU, indent=2)
    schema_str = json.dumps(INTENT_SCHEMA, indent=2)
    
    prompt = f"""
    You are an AI Waiter Logic Engine for an Indian Restaurant.
    Your task is to convert Customer Intent (structured options + free text) into a Kitchen-Ready JSON Ticket.
    
    ### MENU DATA
    {menu_str}
    
    ### INSTRUCTIONS
    1. **Strict Mapping**: Map user requests ONLY to items in the MENU. Do not invent dishes.
    2. **Dietary & Safety**: 
       - If user constraints (e.g., Vegan) conflict with selected item tags (e.g., "Butter Chicken" has "dairy"), set "conflict_flag": true and explain in "conflict_message".
       - If user asks for unsafe food (raw meat, etc.), set "confirm_with_customer": true.
    3. **Taste Profile**: Merge user explicit controls (slider values) with their text request. Text overrides sliders if explicit.
    4. **Output Format**: You MUST output valid JSON strictly matching this schema:
    {schema_str}
    
    5. **Ambiguity**: If the user text is vague (e.g., "Bring me food"), set "confirm_with_customer": true and ask a "clarification_question".
    6. **Confidence**: Score your matching confidence (0.0 to 1.0).
    """
    return prompt

def parse_intent(user_text, structured_inputs, api_key, model_name):
    """
    Main function to parse user intent.
    
    Args:
        user_text (str): Free text input.
        structured_inputs (dict): Dict of UI controls (spice, allergy, etc).
        api_key (str): Groq API Key.
        model_name (str): Selected Model.
        
    Returns:
        dict: The final parsed JSON intent.
    """
    
    system_prompt = generate_system_prompt()
    
    user_message_content = f"""
    ### USER INPUTS
    - Free Text: "{user_text}"
    - Preference Controls: {json.dumps(structured_inputs)}
    
    Generate the Chef Ticket JSON.
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message_content}
    ]
    
    print(f"[DEBUG] Sending request to {model_name}...")
    
    # 1. First Attempt
    response_content, error = call_groq_api(api_key, model_name, messages)
    
    if error:
        logger.error(f"LLM Call Failed: {error}")
        return fallback_logic(user_text, structured_inputs, error_msg=error)
        
    # 2. Parse & Validate
    parsed_json, json_error = try_parse_json(response_content)
    
    # 3. Retry Logic (Self-Correction) if JSON is invalid
    if not parsed_json:
        logger.warning(f"Invalid JSON received: {json_error}. Retrying...")
        messages.append({"role": "assistant", "content": response_content})
        messages.append({"role": "user", "content": f"Your response was not valid JSON: {json_error}. Please fix it and output ONLY valid JSON."})
        
        response_content_retry, error_retry = call_groq_api(api_key, model_name, messages)
        if error_retry:
            return fallback_logic(user_text, structured_inputs, error_msg=error_retry)
            
        parsed_json, json_error = try_parse_json(response_content_retry)
        
    # 4. Final Verification or Fallback
    if parsed_json:
        # Schema check
        is_valid, schema_error = validate_json(parsed_json)
        if is_valid:
            print("[DEBUG] Valid JSON parsed successfully.")
            return parsed_json
        else:
             logger.error(f"Schema Validation Failed: {schema_error}")
             # Even if schema validation fails, we might return partial data or fallback
             # For rigorousness, let's fallback if critical fields are missing
             return fallback_logic(user_text, structured_inputs, error_msg=f"Schema invalid: {schema_error}")
    else:
        logger.error("Retry failed to produce valid JSON.")
        return fallback_logic(user_text, structured_inputs, error_msg="Model failed to produce JSON twice.")


def try_parse_json(content):
    """Attempts to parse JSON from string, handling potential markdown fences."""
    try:
        # Strip markdown fences if present
        cleaned = content.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned.replace("```json", "", 1)
        if cleaned.startswith("```"): # handle case where just ``` is used
             cleaned = cleaned.replace("```", "", 1)
        if cleaned.endswith("```"):
            cleaned = cleaned.replace("```", "", 1)
            
        return json.loads(cleaned), None
    except json.JSONDecodeError as e:
        return None, str(e)

def fallback_logic(user_text, structured_inputs, error_msg="Unknown Error"):
    """
    Deterministic fallback when LLM fails.
    Constructs a basic safe ticket based on structured inputs.
    """
    print(f"[DEBUG] Triggering Fallback logic due to: {error_msg}")
    
    # Try keywords matching from text
    detected_items = []
    all_items = get_all_items_flat()
    lower_text = user_text.lower()
    
    for item in all_items:
        if item['name'].lower() in lower_text:
            detected_items.append({"name": item['name'], "quantity": 1, "notes": "Detected via keyword match"})
            
    return {
        "ordered_items": detected_items,
        "dietary_constraints": structured_inputs.get('diet', []) + structured_inputs.get('allergies', []),
        "taste_profile": {
            "spice_level":  f"Fallback: {structured_inputs.get('spice', 0)}/5",
            "oil_level": structured_inputs.get('oil', 'Unknown'),
             "sweetness": str(structured_inputs.get('sweetness', 0)),
             "salt_level": structured_inputs.get('salt', 'Normal')
        },
        "cooking_notes": "FALLBACK MODE ACTIVE. LLM Failed. Chef please verify order manualy.",
        "confirm_with_customer": True,
        "clarification_question": "Our system is having trouble. Please confirm your order with the staff.",
        "confidence_score": 0.1,
        "ambiguity_reasons": ["LLM Generation Failed", error_msg],
        "conflict_flag": False
    }
