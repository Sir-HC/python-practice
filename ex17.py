#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests 
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'

r = requests.get(url)

r_html = r.text

soup = BeautifulSoup(r_html, 'html5lib')
title = soup.title.string
articles = soup.find_all('article')

for x in articles:
    try:
        aTitle = x.find('h2').string
        print(aTitle)
    except AttributeError:
        continue

input('exit')