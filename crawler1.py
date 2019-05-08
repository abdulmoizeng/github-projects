import urllib.request
from bs4 import BeautifulSoup
import json
import requests
import time


url = "https://example.webscraping.com/"

#user_agent =
#request = urllib.request.urlopen(request) .read()
#html = urllib.request.urlopen(request) .read()
page_response = requests.get(url, timeout=5)
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

main_table = soup.find("div", attrs={'id : pagination'})

urls = []
results = main_table.find_all('a', attrs={'id : pagination'})
for result in results:
    url = result['href']
    if not url.startswith('http'):
        url = "https://example.webscraping.com/" + url
        urls.append(url)
        
     
