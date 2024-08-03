import hashlib
import requests
from urllib.error import URLError, HTTPError

url = 'https://time.is/'

def check_website():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        new_hash = hashlib.sha224(response.content).hexdigest()
        return new_hash
    except requests.exceptions.HTTPError as e:
        raise Exception(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to reach server: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
