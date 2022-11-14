#!/usr/bin/env python
# coding: utf-8

# **Steps**
# 
#     -> Give Business ID to ninox data
# 
#         -> name match with enriched data
#     
#             -> append Business ID to enriched data

# In[410]:


import os
import pandas as pd
import numpy as np 
import difflib
import hashlib
import json
os.getcwd()
os.chdir('/Users/apple/Desktop/cea/diy1111') 


# !pip install name_matching


#Import Data 
# df = pd.read_excel('1017appendinput_564939_Out.xlsx',sheet_name='Sheet1')
# ninox = pd.read_excel('1017appendinput_564939_Out.xlsx',sheet_name='ninox')
df = pd.read_excel('1111appendinput_572484_Out.xlsx',sheet_name='Sheet1')
ninox = pd.read_csv('ninox.csv')


df=df.iloc[1:,]



# Fill empty Enhanced Business Name with name of the firm
ninox['Enhanced Business Name'].fillna(ninox['Name of the Firm'], inplace=True)


# create unique keys based on business name 
z = np.empty((0, 2))
bn = ninox['Enhanced Business Name'].unique() 

for row in bn:
    y = hashlib.sha1(json.dumps(row).encode()).hexdigest()
    z = np.append(z,np.array([[row, y]]), axis = 0 )
    z = pd.DataFrame(z, columns = ['BUSINESSNAME','Business_ID'])


ninox1=pd.merge(ninox,z,left_on='Enhanced Business Name',right_on='BUSINESSNAME',how='left')




# Set up name matcher
from name_matching.name_matcher import NameMatcher
matcher = NameMatcher(top_n=10,
    lowercase=False,
    punctuations=False,
    remove_ascii=True,
    legal_suffixes=False,
    common_words=False,
    verbose=True)
matcher.set_distance_metrics(['discounted_levenshtein',
                              'SSK', 
                              'fuzzy_wuzzy_token_sort'])


# Match with business name
matcher.load_and_process_master_data('Enhanced Business Name', ninox)
match_table=matcher.match_names(to_be_matched=df, column_matching='ENHANCEDBUSINESSNAME')



match_table
# Original_name = Enhanced Business Name in 1022enrich data
# Match_name = Enhanced Business Name in Ninox
# Ground UP Builders -> Ground Up Builders and Design Inc
# Northbay Home Construction Solutions INC	Cornerstone Construction Solutions INC


# Pick rows with score above 80
match_table2 = match_table[ (match_table['score'] > 80) ]



# Merge table with ninox data
match_table3=pd.merge(match_table2,ninox1,left_on='match_name',right_on='Enhanced Business Name',how='left')


# Get the name and business_ID for the enriched data and append the business id to it.
match_table4 = match_table3.iloc[:,[0,1,-1]]
df_final=pd.merge(df,match_table4,left_on='ENHANCEDBUSINESSNAME',right_on='original_name',how='left')



df_final1 = df_final.drop_duplicates()


# Drop rows with empty business_ID
df_final2 = df_final1.dropna(subset=['Business_ID'])
# df_final[df_final['Business_ID'].isna()].shape


#df_final2.to_csv('1028append2_bID.csv')
#ninox1.to_csv('ninox_bID.csv')






# ## Corner cases


# Find business with empty business ID
df_case = df_final1[df_final1['Business_ID'].isna()]



# Match with property add
matcher.load_and_process_master_data('Address', ninox)
match_table_=matcher.match_names(to_be_matched=df_case, column_matching='PROPERTYADDRESSFULL2')



# Merge with ninox data on property address
df_case = df_case.drop(columns=['Business_ID'])
ninox_add = ninox1[['Address','Business_ID']]
df_case1 = pd.merge(df_case,ninox_add,left_on='PROPERTYADDRESSFULL2',right_on='Address',how='left')


# In[436]:


# Remove duplicate columns
df_case1=df_case1.drop_duplicates('BUSINESSNAME')



df_case1=df_case1.drop(columns=['Address'])



# Combine two dataframes
result = pd.concat([df_final2, df_case1])


result.to_csv('data_enriched_bID.csv')
ninox1.to_csv('ninox_bID.csv')
