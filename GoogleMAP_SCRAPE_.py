#!/usr/bin/env python
# coding: utf-8
import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
# !pip install google-search-results
from serpapi import GoogleSearch


# ## Boston

params = {
  "engine": "google_maps",
  "q": "stone masonry, boston",
  "ll": "@42.368251,-71.5225592,10z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":0
}
# Change Name, Latitude, Longtitude if you want to search other things in other cities.
# Latitude, Longtitude can be found on the google map link


data=[]
for i in range(20,100,20):
    params['start']=i
    search = GoogleSearch(params)
    results = search.get_dict()

    local_results = results["local_results"]
    

    for item in local_results:
        try:
            data.append([item['title'], item['phone'],item['address']])
        except:
            pass


# ## Los Angeles CA

params = {
  "engine": "google_maps",
  "q": "stone masonry, Los Angeles",
  "ll": "@34.0025531,-118.4262034,9.52z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":0
}

for i in range(20,100,20):
    params['start']=i
    search = GoogleSearch(params)
    results = search.get_dict()

    local_results = results["local_results"]
    

    for item in local_results:
        try:
            data.append([item['title'], item['phone'],item['address']])
        except:
            pass


# ## Atlanta GA

params = {
  "engine": "google_maps",
  "q": "stone masonry, Atlanda",
  "ll": "@33.7820232,-84.5261447,9.81z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":0
}

for i in range(20,100,20):
    params['start']=i
    search = GoogleSearch(params)
    results = search.get_dict()

    local_results = results["local_results"]
    

    for item in local_results:
        try:
            data.append([item['title'], item['phone'],item['address']])
        except:
            pass


# ## Mineapolis St Paul MN

params = {
  "engine": "google_maps",
  "q": "stone masonry, Mineapolis St Paul MN",
  "ll": "@44.9922454,-93.4040169,9.28z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":0
}

for i in range(20,100,20):
    params['start']=i
    search = GoogleSearch(params)
    results = search.get_dict()

    local_results = results["local_results"]
    

    for item in local_results:
        try:
            data.append([item['title'], item['phone'],item['address']])
        except:
            pass


# ## Houston TX

params = {
  "engine": "google_maps",
  "q": "stone masonry, Houston TX",
  "ll": "@29.7674228,-95.524256,9.68z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":0
}

for i in range(20,100,20):
    params['start']=i
    search = GoogleSearch(params)
    results = search.get_dict()

    local_results = results["local_results"]
    

    for item in local_results:
        try:
            data.append([item['title'], item['phone'],item['address']])
        except:
            pass


df = pd.DataFrame(data, columns=['Business Name', 'Phone','Address'])
df.to_excel('google_map_scrape_data.xlsx')
