import requests as rq
from time import sleep
import json

from config import REQUEST_HEADERS


def get(url: str, retries=3, delay=2) -> str:
    headers_json = json.loads(REQUEST_HEADERS)
    
    for _ in range(retries):
        try:
            response = rq.get(url=url, headers=headers_json, timeout=5)
            response.raise_for_status()
            
            return response.text
        except rq.RequestException:
            sleep(delay)
    
    raise Exception(f"Failed to fetch {url}")