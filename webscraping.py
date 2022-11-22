#!/usr/bin/env python
# coding: utf-8

import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


url_df=pd.DataFrame()

#Might need to change headers for windows
headers = {'User-Agent':'Mozilla/5.0'}


url1='https://www.bbb.org/search?filter_distance=50&find_country=USA&find_latlng=42.335392%2C-71.078356&find_loc=Boston%2C%20MA&find_text=stone%20masonry&page='

url2='https://www.bbb.org/search?find_country=USA&find_latlng=34.042062%2C-118.298181&find_loc=Los%20Angeles%2C%20CA&find_text=stone%20masonry&page='

url3='https://www.bbb.org/search?find_country=USA&find_loc=Atlanta&find_text=stone%20masonry&page='

url4='https://www.bbb.org/search?find_country=USA&find_latlng=44.986693%2C-93.291378&find_loc=Minneapolis%2C%20MN&find_text=stone%20masonry&page='

url5='https://www.bbb.org/search?find_country=USA&find_latlng=29.722552%2C-95.425335&find_loc=Houston%2C%20TX&find_text=stone%20masonry&page='


for page in range(1,7):
    try:
        k=url1 + str(page) + '&sort=Relevance'
        print(k)

        r = requests.get(k, headers = headers)
        print(r)
    #   PATTERN
        p = re.compile(r'PRELOADED_STATE__ = (.*?);')

    #   Load data
        data = json.loads(p.findall(r.text)[0])

        results = [(item['businessName'], item['address'],item['city'], item['state'], item['postalcode'], item['phone']) for item in data['searchResult']['results']]

    #   Convert to dataframe
        df = pd.DataFrame(results, columns=['Business Name', 'Address','City', 'State', 'Zip', 'Phone'])

    #   Append data
        url_df=url_df.append(df)
        time.sleep(30)
    except:
        time.sleep(30)
        pass
    


for page in range(1,3):
    try:
        k=url2 + str(page) + '&sort=Relevance'
        print(k)

        r = requests.get(k, headers = headers)
        print(r)
    #   PATTERN
        p = re.compile(r'PRELOADED_STATE__ = (.*?);')

    #   Load data
        data = json.loads(p.findall(r.text)[0])

        results = [(item['businessName'], item['address'],item['city'], item['state'], item['postalcode'], item['phone']) for item in data['searchResult']['results']]

    #   Convert to dataframe
        df = pd.DataFrame(results, columns=['Business Name', 'Address','City', 'State', 'Zip', 'Phone'])

    #   Append data
        url_df=url_df.append(df)
        time.sleep(30)
    except:
        time.sleep(30)
        pass


for page in range(1,5):
    try:
        k=url3 + str(page) + '&sort=Relevance'
        print(k)

        r = requests.get(k, headers = headers)
        print(r)
    #   PATTERN
        p = re.compile(r'PRELOADED_STATE__ = (.*?);')

    #   Load data
        data = json.loads(p.findall(r.text)[0])

        results = [(item['businessName'], item['address'],item['city'], item['state'], item['postalcode'], item['phone']) for item in data['searchResult']['results']]

    #   Convert to dataframe
        df = pd.DataFrame(results, columns=['Business Name', 'Address','City', 'State', 'Zip', 'Phone'])

    #   Append data
        url_df=url_df.append(df)
        time.sleep(30)
    except:
        time.sleep(30)
        pass


for page in range(1,3):
    try:
        k=url4 + str(page) + '&sort=Relevance'
        print(k)

        r = requests.get(k, headers = headers)
        print(r)
    #   PATTERN
        p = re.compile(r'PRELOADED_STATE__ = (.*?);')

    #   Load data
        data = json.loads(p.findall(r.text)[0])

        results = [(item['businessName'], item['address'],item['city'], item['state'], item['postalcode'], item['phone']) for item in data['searchResult']['results']]

    #   Convert to dataframe
        df = pd.DataFrame(results, columns=['Business Name', 'Address','City', 'State', 'Zip', 'Phone'])

    #   Append data
        url_df=url_df.append(df)
        time.sleep(30)
    except:
        time.sleep(30)
        pass


for page in range(1,3):
    try:
        k=url5 + str(page) + '&sort=Relevance'
        print(k)

        r = requests.get(k, headers = headers)
        print(r)
    #   PATTERN
        p = re.compile(r'PRELOADED_STATE__ = (.*?);')

    #   Load data
        data = json.loads(p.findall(r.text)[0])

        results = [(item['businessName'], item['address'],item['city'], item['state'], item['postalcode'], item['phone']) for item in data['searchResult']['results']]

    #   Convert to dataframe
        df = pd.DataFrame(results, columns=['Business Name', 'Address','City', 'State', 'Zip', 'Phone'])

    #   Append data
        url_df=url_df.append(df)
        time.sleep(30)
    except:
        time.sleep(30)
        pass


#Correct values
url_df['Business Name']=url_df['Business Name'].str.replace('</em>','')
url_df['Business Name']=url_df['Business Name'].str.replace('<em>','')
url_df['Phone']=url_df['Phone'].astype(str).apply(lambda x: x.replace('[','').replace(']','')) 


url_df.to_excel('outputfile.xlsx')

