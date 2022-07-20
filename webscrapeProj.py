#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
#import pandas as pd

url = 'https://www.aquabid.com/cgi-bin/auction/auction.cgi?fwcatfishp&&&&&&&pb=100'

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#table = soup.find_all("td")
#table = soup.find_all("tbody")
table = soup.find_all("tr")
#option = soup.find_all("td")

for tag in table:
    print(tag.text)
