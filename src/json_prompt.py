import json
import os

# Load the JSON prompt from the file
file_path = os.path.join('src', 'prompt.json')
try:
    with open(file_path, 'r') as f:
        prompt_data = json.load(f)
except FileNotFoundError:
    print("Error: 'prompt.json' not found.")
    exit()

# Function to construct the complete system prompt from JSON
def construct_prompt(prompt_dict):
    """
    Constructs a comprehensive prompt string from the JSON dictionary.
    """
    prompt_parts = []
    
    # Add Task and Persona
    prompt_parts.append(f"Task: {prompt_dict['task']}")
    prompt_parts.append(f"Persona: {prompt_dict['persona']['description']}")

    # Add Guard Rails
    prompt_parts.append("\n--- Strict Guard Rails ---")
    for key, value in prompt_dict['guard_rails'].items():
        prompt_parts.append(f"{key}: {value}")

    # Add Instructions
    prompt_parts.append("\n--- Instructions ---")
    for instruction in prompt_dict['instructions']:
        prompt_parts.append(f"- {instruction}")

    # Add Knowledge Base
    prompt_parts.append("\n--- Knowledge Base (DO NOT DEVIATE) ---")
    # This is a simplified way to add the knowledge base.
    # For a more robust solution, you would iterate through each sub-section.
    prompt_parts.append(json.dumps(prompt_dict['knowledge_base'], indent=2))
    
    return "\n".join(prompt_parts)

json_prompt = construct_prompt(prompt_data)