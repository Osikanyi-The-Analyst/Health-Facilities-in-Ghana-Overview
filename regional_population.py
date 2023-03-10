# importing libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

URL = 'https://en.wikipedia.org/wiki/List_of_Ghanaian_regions_by_population'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}


page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup2)

table=soup2.find(class_='wikitable sortable')
table

headers = [th.text.strip() for th in table.find_all('th')]
headers

headers

data = []
for tr in table.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all('td')]
    if row:
        data.append(row)

data

import pandas as pd
df = pd.DataFrame(data, columns=headers)
df

#Data cleaning looks small and I prefer to do what left with Ms Excel

df.to_csv('regional_population.csv')


