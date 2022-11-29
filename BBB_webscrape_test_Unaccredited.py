#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# In[3]:



headers = {'User-Agent':'Mozilla/5.0'}

#URL
url='https://www.bbb.org/search?find_country=USA&find_latlng=42.335392%2C-71.078356&find_loc=Boston%2C%20MA&find_text=stone%20masonry&page=1&sort=Rating&touched=2'
r = requests.get(url, headers = headers)
#Open chrome brower
driver = webdriver.Chrome()
driver.get(url)


# In[ ]:



#locate the button and automatically click it
el=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/label/span[1]/span[1]/input")
el.click()


# In[4]:


page_content = driver.page_source


# In[5]:


page_content


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


results = []

for el in response.xpath('//*[@id="content"]/div/div[3]/div/div[1]/div[2]/div[7]/div/div[1]/div[1]/h3/a/span'):
    results.append({
#         'link': el.xpath('./a/@href').extract_first(''),
        'text': el,
        'title': el.xpath('text()').extract_first('')
    })

print(results)


# In[ ]:


r.text


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


url='https://www.bbb.org/search?find_country=USA&find_latlng=42.335392%2C-71.078356&find_loc=Boston%2C%20MA&find_text=stone%20masonry&page=1&sort=Rating&touched=12'


# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get(url)


# In[ ]:


el=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/label/span[1]/span[1]/input")
el.click()


# In[ ]:



headers = {'User-Agent':'Mozilla/5.0'}

#URL
r = requests.get('https://www.bbb.org/search?filter_distance=50&find_country=USA&find_latlng=42.335392%2C-71.078356&find_loc=Boston%2C%20MA&find_text=stone%20masonry&page=2&sort=Relevance', headers = headers)

#PATTERN
p = re.compile(r'PRELOADED_STATE__ = (.*?);')


# In[ ]:


# # p.findall(r.text)[0]
# #Load data
# data = json.loads(p.findall(r.text)[0])

# p.findall(r.text)[0]


with open('readme1.txt', 'a') as f:
    f.write(''.join(p.findall(r.text)[0]))


# In[ ]:


with open("readme.txt", 'r') as f:
    raw_data = f.read()


# In[ ]:


# raw_data[10000:]


# In[ ]:


index_of_the_end_of_last_record = 100 # For example
data = json.loads(raw_data)


# In[ ]:


df=pd.DataFrame()
results = [(item['businessName'], item['address'],item['city'], item['state'], item['postalcode'], item['phone']) for item in data['searchResult']['results']]

#Convert to dataframe
df = pd.DataFrame(results, columns=['Business Name', 'Address','City', 'State', 'Zip', 'Phone'])


# In[ ]:





# In[ ]:


# p.findall(r.text)[0]
df


# result


# In[ ]:





# In[ ]:


#Correct values
df['Business Name']=df['Business Name'].str.replace('</em>','')
df['Business Name']=df['Business Name'].str.replace('<em>','')


# In[ ]:


df


# In[ ]:





# In[ ]:


url1='https://www.bbb.org/search?filter_distance=50&find_country=USA&find_latlng=42.335392%2C-71.078356&find_loc=Boston%2C%20MA&find_text=stone%20masonry&page='


# In[ ]:


url1


# In[ ]:


import time
# time.sleep(3)


# In[ ]:


url_df=pd.DataFrame()
for page in range(1,7):
    try:
        k=url1 + str(page) + '&sort=Relevance'
        print(k)
        headers = {'User-Agent':'Mozilla/5.0'}

    #     #URL
        r = requests.get(k, headers = headers)
        print(r)
    #     #PATTERN
        p = re.compile(r'PRELOADED_STATE__ = (.*?);')

    #     #Load data
        data = json.loads(p.findall(r.text)[0])

        results = [(item['businessName'], item['address'],item['city'], item['state'], item['postalcode'], item['phone']) for item in data['searchResult']['results']]

    #     #Convert to dataframe
        df = pd.DataFrame(results, columns=['Business Name', 'Address','City', 'State', 'Zip', 'Phone'])

        url_df=url_df.append(df)
        time.sleep(20)
    except:
        pass
    
    


# In[ ]:


url_df


# In[ ]:


https://www.bbb.org/search?filter_distance=50&find_country=USA&find_latlng=42.335392%2C-71.078356&find_loc=Boston%2C%20MA&find_text=stone%20masonry&page=15&sort=Relevance
    


# In[ ]:


url_df[:2]


# In[ ]:





# In[ ]:


# df.to_csv('data.csv')

