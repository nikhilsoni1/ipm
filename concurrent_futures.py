import concurrent.futures
from re import S
import requests
from datetime import datetime
import pandas as pd

URLS = ['https://www.foxnews.com/',
        'https://www.cnn.com/',
        'https://europe.wsj.com/',
        'https://www.bbc.co.uk/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with requests.get(url, timeout=timeout) as response:
        return f"{response.status_code}"

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url.get(future)
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print(f"{url} page is {len(data)} bytes, {datetime.now():%f}")