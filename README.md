# AI Waiter Prototype (Indian Restaurant)

This project is a prototype for an AI-powered smart waiter system. It takes customer natural language orders (e.g., "I want something spicy and creamy") along with structured preferences (Diet, Allergies) and generates a precise, kitchen-ready ticket for the chef using the Groq LLM.

## Features

- **Customer View**: Interactive menu, preference sliders (spice, oil), allergy controls, and chat input.
- **Chef View**: Structured, unambiguous instructions including cooking notes and safety warnings.
- **AI Logic**: Uses Groq (Llama3/Mixtral) to map matches to a static Indian menu.
- **Safety**: Detects allergy conflicts (e.g., Vegan vs Butter Chicken) and asks for confirmation if ambiguous.
- **Fallback**: Includes a rule-based fallback if the AI fails to generate valid JSON.

## Prerequisites

- Python 3.8 or higher installed.
- A [Groq API Key](https://console.groq.com/keys).

## Setup (Windows)

1.  **Open Terminal** (Powershell or CMD) in this folder.

2.  **Create a Virtual Environment**:
    ```powershell
    python -m venv .venv
    ```

3.  **Activate the Environment**:
    ```powershell
    .\.venv\Scripts\activate
    ```

4.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```

## Running the App

1.  **Start the Server**:
    ```powershell
    python app.py
    ```

2.  **Open Browser**:
    - The terminal will show a local URL, usually `http://127.0.0.1:7860`.
    - Open this link in Chrome/Edge.

## Usage

1.  **Enter API Key**:
    - You can paste your Groq API Key in the "Groq API Key" box on the top left.
    - *Alternatively*, set it in your environment: `$env:GROQ_API_KEY="your_key"` before running python.

2.  **Place Order**:
    - Browse the menu (Accordion).
    - Set your spice/oil preferences.
    - Select any allergies.
    - Type your order in the text box (e.g., "One butter chicken and 2 garlic naans").
    - Click **Send to Chef**.

3.  **View Output**:
    - The right panel will show the "Visual Ticket" for the kitchen and the raw structured JSON.
    - Look out for Yellow (Conflict) or Red (Confirm) warnings!

## Troubleshooting

- **"Module not found" error**: Ensure you activated the `.venv` before running `python app.py`.
- **API Error**: Check your internet connection and verify your Groq API Key is valid.
- **JSON Error**: If the model frequently fails, try switching to a larger model like `llama3-70b` using the dropdown.