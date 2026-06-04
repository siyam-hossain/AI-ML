'''
Real-world example: Multi-threading for io bound tasks
Scenario: Web scraping
Web scraping often involves making numerous network requests to fetch web pages.
These tasks are io bound because they spend a lot of time waiting for responses for servers. 
Multi-threading can significantly improve the performance by allowing multiple web pages to be fetched concurrently
'''

# https://docs.langchain.com/
# https://docs.langchain.com/oss/python/langchain/quickstart
# https://docs.langchain.com/oss/python/langchain/agents

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://docs.langchain.com/',
    'https://docs.langchain.com/oss/python/langchain/quickstart',
    'https://docs.langchain.com/oss/python/langchain/agents'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
    # print(soup.contents)
    print()


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print("All web pages fetched")