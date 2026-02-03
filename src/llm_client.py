# src/llm_client.py

import requests
import json
import time

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def call_groq_api(api_key, model_name, messages, temperature=0.1):
    """
    Calls the Groq API to get a chat completion.
    
    Args:
        api_key (str): The Groq API key.
        model_name (str): The model to use (e.g., 'llama3-70b-8192').
        messages (list): List of message dicts (role, content).
        temperature (float): Sampling temp, low for deterministic output.
        
    Returns:
        dict: The parsed JSON response content if successful, or None.
        str: Raw text content if JSON parsing fails but request succeeded.
        str: Error message if request failed.
    """
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model_name,
        "messages": messages,
        "temperature": temperature,
        "response_format": {"type": "json_object"} # Force JSON mode if model supports it
    }
    
    try:
        start_time = time.time()
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        latency = time.time() - start_time
        
        # Log latency (in a real app, use logger)
        print(f"[DEBUG] LLM Latency: {latency:.2f}s")
        
        response.raise_for_status()
        
        data = response.json()
        content = data['choices'][0]['message']['content']
        
        return content, None  # Success, no error
        
    except requests.exceptions.RequestException as e:
        error_msg = f"API Request Failed: {str(e)}"
        if hasattr(e, 'response') and e.response is not None:
            error_msg += f" | Response: {e.response.text}"
        return None, error_msg
    except Exception as e:
        return None, f"Unexpected Error: {str(e)}"
