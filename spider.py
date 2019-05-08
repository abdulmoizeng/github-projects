""
Follow following link and do below mention steps one by one
 https://github.com/abdulmoizeng/crawlers-demo/blob/master/crawler-demo/spider2.py

Steps: 
- Crawl main page and collect all available urls in a variable
- Crawl one by one available urls and add those in the list 
- Now visit newly added urls and append all url's list
- set a threshold let's say 1000 urls when reached stop the crawling process

By following above steps at the end you would have all 1000 urls stored in a list,

Now iterate through the list and visit each page once and make an inverted index for each word available with respect to the page

once one page visit is completed save it in a file and then repeat the page visit process at a time gap of 5 seconds

At last you will have all the required info

"""

import requests
from parsel import Selector

import time
start = time.time()

all_links  = [] 
# GET request to recurship site
response = requests.get('http://example.webscraping.com/')
selector = Selector(response.text)
href_links = selector.xpath('//a/@href').getall()
all_links += href_links

for link in href_links:
    try:
        response = requests.get(link)
        selector = Selector(response.text)
        href_links = selector.xpath('//a/@href').getall()
        all_links += href_links
        if len(all_links) >=1000:
          break
    except Exception as exp:
        print('Error navigating to link : ', link)


# Here "all_links" should have 1000 links in it


print(all_images)
end = time.time()
print("Time taken in seconds : ", (end-start))
