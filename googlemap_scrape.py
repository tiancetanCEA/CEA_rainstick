#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
# !pip install google-search-results
from serpapi import GoogleSearch


# ## Boston

# In[2]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, boston",
  "ll": "@42.368251,-71.5225592,10z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  #"start":20
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]


# In[3]:


data=[]


# In[4]:


for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[ ]:





# In[7]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, boston",
  "ll": "@42.3632658,-71.0720349,12.22z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":20
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[9]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, boston",
  "ll": "@42.3632658,-71.0720349,12.22z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":40
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[10]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, boston",
  "ll": "@42.3632658,-71.0720349,12.22z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":60
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[11]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, boston",
  "ll": "@42.3632658,-71.0720349,12.22z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":80
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[15]:



df = pd.DataFrame(data, columns=['Business Name', 'Phone','Address'])


# In[16]:


# df


# ## Los Angeles CA

# In[95]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Los Angeles",
  "ll": "@34.0025531,-118.4262034,9.52z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[99]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Los Angeles",
  "ll": "@34.0025531,-118.4262034,9.52z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":20
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[100]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Los Angeles",
  "ll": "@34.0025531,-118.4262034,9.52z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":40
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[101]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Los Angeles",
  "ll": "@34.0025531,-118.4262034,9.52z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":60
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[102]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Los Angeles",
  "ll": "@34.0025531,-118.4262034,9.52z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":80
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# ## Atlanta GA

# In[105]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Atlanda",
  "ll": "@33.7820232,-84.5261447,9.81z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[108]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Atlanda",
  "ll": "@33.7820232,-84.5261447,9.81z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":20
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[109]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Atlanda",
  "ll": "@33.7820232,-84.5261447,9.81z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":40
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[110]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Atlanda",
  "ll": "@33.7820232,-84.5261447,9.81z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":60
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[111]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Atlanda",
  "ll": "@33.7820232,-84.5261447,9.81z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":80
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# ## Mineapolis St Paul MN

# In[114]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Mineapolis St Paul MN",
  "ll": "@44.9922454,-93.4040169,9.28z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  #"start":80
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[117]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Mineapolis St Paul MN",
  "ll": "@44.9922454,-93.4040169,9.28z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":20
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[118]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Mineapolis St Paul MN",
  "ll": "@44.9922454,-93.4040169,9.28z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":40
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[119]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Mineapolis St Paul MN",
  "ll": "@44.9922454,-93.4040169,9.28z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":60
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[120]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Mineapolis St Paul MN",
  "ll": "@44.9922454,-93.4040169,9.28z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":80
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# ## Houston TX

# In[123]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Houston TX",
  "ll": "@29.7674228,-95.524256,9.68z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  #"start":80
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[126]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Houston TX",
  "ll": "@29.7674228,-95.524256,9.68z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":20
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[127]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Houston TX",
  "ll": "@29.7674228,-95.524256,9.68z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":40
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[128]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Houston TX",
  "ll": "@29.7674228,-95.524256,9.68z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":60
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[129]:


params = {
  "engine": "google_maps",
  "q": "stone masonry, Houston TX",
  "ll": "@29.7674228,-95.524256,9.68z",
  "type": "search",
  "api_key": "fcb97729c82095114593917c27518759909045f550685c5cbaf2f17e67237ad5",
  "start":80
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]
# data=[]

for item in local_results:
    try:
        data.append([item['title'], item['phone'],item['address']])
    except:
        pass


# In[ ]:





# In[ ]:





# In[142]:



df = pd.DataFrame(data, columns=['Business Name', 'Phone','Address'])


# In[147]:


df


# In[146]:


# df['Phone'] = df['Phone'].str.replace('+1','')
df['Phone'] = df['Phone'].str.replace('[^\w\s]','')


# In[ ]:





# In[148]:


df.to_excel('google_map_scrape_data.xlsx')


# In[ ]:




