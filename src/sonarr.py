import requests

def get_series(sonarr_url, sonarr_api_key, output_file):
    headers = {'X-Api-Key': sonarr_api_key}
    endpoint = f'{sonarr_url}/api/v3/series'
    
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except Exception as e:
        raise Exception(f"Failed to get response from Sonarr server: {e}")
    
    series_list = response.json()
    
    with open(output_file, 'w', encoding='utf-8') as txtfile:
        for series in series_list:
            title = series.get('title')
            if title:  
                txtfile.write(title + '\n')

def read_file(output_file):
    with open(output_file, 'r', encoding='utf-8') as txtfile:
        content = txtfile.readlines()
    return ''.join(content)