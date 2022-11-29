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


headers = {'User-Agent':'Mozilla/5.0'}

#URL
url='https://www.bbb.org/search?find_country=USA&find_latlng=42.335392%2C-71.078356&find_loc=Boston%2C%20MA&find_text=stone%20masonry&page=1&sort=Rating&touched=2'
r = requests.get(url, headers = headers)
#Open chrome brower
driver = webdriver.Chrome()
driver.get(url)


#locate the button and automatically click it
el=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/label/span[1]/span[1]/input")
el.click()


page_content = driver.page_source


page_content

