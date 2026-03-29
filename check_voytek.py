import requests
import time

def check_website(url):
    start_time = time.time()
    response = requests.get(url)

    if response.status_code == 200:
        end_time = time.time()
        response_time = end_time - start_time
        print(f"Website {url} is online with a response time of {response_time:.6f} seconds.")
    else:
        print(f"Website {url} is offline (Status code: {response.status_code})")

check_website("https://voytek.ai")
