# import requests
# import threading
# import time

# URL = "http://localhost:8080/shorten"
# NUM_REQUESTS = 10000    # total requests
# CONCURRENCY = 10       # how many threads run in parallel

# def shorten_url():
#     data = {"url": "https://openai.com"}
#     try:
#         response = requests.post(URL, json=data)
#         print(f"[{response.status_code}] {response.json()}")
#     except Exception as e:
#         print(f"Error: {e}")

# def worker():
#     for _ in range(NUM_REQUESTS // CONCURRENCY):
#         shorten_url()

# if __name__ == "__main__":
#     start = time.time()
#     threads = []

#     for _ in range(CONCURRENCY):
#         t = threading.Thread(target=worker)
#         t.start()
#         threads.append(t)

#     for t in threads:
#         t.join()

#     end = time.time()
#     print(f"Completed {NUM_REQUESTS} requests in {end - start:.2f} seconds")


import requests
import threading
import time
import argparse

# Parse the command-line argument
parser = argparse.ArgumentParser(description="Stress test the URL shortener")
parser.add_argument("url_to_shorten", help="The URL to shorten")
args = parser.parse_args()

# Constants
API_ENDPOINT = "http://localhost:8080/shorten"
NUM_REQUESTS = 100
CONCURRENCY = 10

def shorten_url():
    data = {"url": args.url_to_shorten}
    try:
        response = requests.post(API_ENDPOINT, json=data)
        print(f"[{response.status_code}] {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

def worker():
    for _ in range(NUM_REQUESTS // CONCURRENCY):
        shorten_url()

if __name__ == "__main__":
    start = time.time()
    threads = []

    for _ in range(CONCURRENCY):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.time()
    print(f"Completed {NUM_REQUESTS} requests in {end - start:.2f} seconds")
