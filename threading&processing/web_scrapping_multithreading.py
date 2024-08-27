import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://docs.smith.langchain.com/',
    'https://langchain-ai.github.io/langgraph/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content , 'html.parser')
    print(f"Fetched {len(soup.text)} charcters form {url}")

threads = []

'''' in this loop we are iterating through each url, paassing each url to fetch_content function and creating its thread and append it to the THREADS list, also starting it'''
for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

'''here we are waiting for each thread to execute completely'''
for thread in threads:
    thread.join()

print("Fetching completed")