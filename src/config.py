import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "sonarr": {
        "url": os.getenv('SONARR_URL', 'http://localhost:8989'),
        "api_key": os.getenv('SONARR_API_KEY', 'default_api_key'),
        "output_file": os.getenv('OUTPUT_FILE', 'output/series.txt'),
    },
    "litellm": {
        "url": os.getenv('LITELLM_URL', 'http://localhost:8000'),
        "api_key": os.getenv('LITELLM_API_KEY', "default_api_key"),
        "model": os.getenv('LITELLM_MODEL', 'gpt-4o'),
        "prompt_template": os.getenv('PROMPT', """
            Instructions:
            I have a CSV list of TV shows that I have already watched. My preference is for apocalyptic or sci-fi TV shows. Based on my existing list, recommend 5 new TV shows (that are not already on my list) that I might also enjoy. 
            Task:
            Recommend 5 new apocalyptic or sci-fi TV shows that are not already on my list. The recommendations should align with my preference for these genres. Please ensure that the recommended shows are not duplicates of those listed.
        """)
    }
}