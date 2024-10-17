from src.config import CONFIG
from src.sonarr import get_series, read_file
from src.llm import send_to_llm
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

def main():
    try:
        sonarr_config = CONFIG['sonarr']
        litellm_config = CONFIG['litellm']

        logging.info("Getting series from Sonarr..." + sonarr_config['url'])
        get_series(sonarr_config['url'], sonarr_config['api_key'], sonarr_config['output_file'])

        logging.info("Reading Sonarr output file...")
        file_content = read_file(sonarr_config['output_file'])

        result = send_to_llm(
            file_content, 
            litellm_config['prompt_template'], 
            litellm_config['api_key'], 
            litellm_config['model'], 
            litellm_config['url']
        )

        text = result['choices'][0]['text']
        total_tokens = result['usage']['total_tokens']

        logging.info(f"Response from LLM: \n\n{text}")
        logging.info(f"Total tokens used: {total_tokens}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
