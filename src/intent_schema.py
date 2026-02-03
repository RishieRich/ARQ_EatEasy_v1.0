# src/intent_schema.py

import json

# Define the schema for the LLM output.
# This ensures we get structured data that we can programmatically handle.

INTENT_SCHEMA = {
    "type": "object",
    "properties": {
        "ordered_items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Exact name of the item from the menu"},
                    "quantity": {"type": "integer"},
                    "notes": {"type": "string", "description": "Specific adjustments for this item"}
                },
                "required": ["name", "quantity"]
            }
        },
        "dietary_constraints": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of strictly identified constraints e.g., 'Vegan', 'No Onion', 'Nut Allergy'"
        },
        "taste_profile": {
            "type": "object",
            "properties": {
                "spice_level": {"type": "string", "enum": ["Low", "Medium", "High", "Very High"]},
                "oil_level": {"type": "string", "enum": ["Low", "Medium", "High"]},
                "sweetness": {"type": "string", "enum": ["Low", "Medium", "High"]},
                "salt_level": {"type": "string", "enum": ["Low", "Normal", "High"]}
            }
        },
        "cooking_notes": {
            "type": "string",
            "description": "General cooking instructions for the chef."
        },
        "confirm_with_customer": {
            "type": "boolean",
            "description": "True if the request is ambiguous or dangerous."
        },
        "clarification_question": {
            "type": "string",
            "description": "If confirm_with_customer is True, what to ask the customer."
        },
        "confidence_score": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "Confidence in understanding the intent."
        },
        "ambiguity_reasons": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of reasons why confidence is not 1.0"
        },
         "conflict_flag": {
            "type": "boolean",
            "description": "True if user constraints conflict with selected item ingredients (e.g. Nuts allergy + Cashew curry)."
        },
        "conflict_message": {
             "type": "string",
             "description": "Message explaining the conflict if conflict_flag is true."
        }
    },
    "required": ["ordered_items", "dietary_constraints", "taste_profile", "confirm_with_customer", "confidence_score"]
}

def validate_json(json_data):
    """
    Very basic validation helper. 
    In a real app, use 'jsonschema' lib, but we are keeping it pure python as requested.
    Returns: (is_valid, error_message)
    """
    try:
        # Check required fields
        for field in INTENT_SCHEMA["required"]:
            if field not in json_data:
                return False, f"Missing required field: {field}"
        
        # Check ordered_items structure
        if not isinstance(json_data.get("ordered_items", []), list):
             return False, "ordered_items must be a list"
             
        return True, ""
    except Exception as e:
        return False, str(e)
