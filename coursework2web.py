from bs4 import BeautifulSoup
import requests
import sys
import urllib3
import itertools
import re
#from urlparse import urljoin


def download(url, user_agent='wswp', num_retries=2):
    print ('Downloading:', url)
    headers = {'User-agent': user_agent}
    request = urllib3.Request(url, headers=headers)
    try:
        html = urllib3.urlopen(request) .read()
    except urllib3.URLERROR as e:
        print ('Download Error:', e.reason)
    html = None
    if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html

def crawl_website(url):
    website = download(url)
    links = re.findall('<loc>(.*?)</loc>', website)
    for link in links:
        html = download(link)

    max_errors = 5
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/' 
        html = download(url)
        if html is None:
            num_errors +=1
        if num_errors == max_errors:
            break
        
    else:
        num_errors = 0

def link_crawler(seed_url, link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urllib.parse.urljoin(seed_url, link)
            if link not in seen:
                seen.add(link)
                crawl_queue.append(link)