import requests

def send_to_llm(file_content, prompt_template, litellm_api_key, litellm_model, litellm_url):
    prompt = f"{prompt_template}\n{file_content}"

    headers = {
        'Authorization': f'Bearer {litellm_api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        "prompt": prompt,
        "model": litellm_model
    }

    full_url = f"{litellm_url}/v1/completions"

    #debug
    # print(f"Sending POST request to URL: {full_url}")
    # print(f"Headers: {headers}")
    # print(f"Data: {data}")

    response = requests.post(full_url, json=data, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to get response from LLM server: {response.status_code}")

    return response.json()