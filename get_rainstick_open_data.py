#!/usr/bin/env python
# coding: utf-8

# ## Step
# ### 1. Match with Name of the Firm 
# ### 2. Match with Enhanced Businss Name
# ### 3. Use Business name match script to match business names
# ### 4. Combine all rows


import os
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Read the csv file which name starts with 'Streak Export'
parent_path = os.listdir('/Users/apple/Desktop/cea/rank/rank11-11') 

df = []
for file in parent_path:
    if file.startswith("Streak Export"):
        df.append(file)
#print(df)


df = pd.read_csv('/Users/apple/Desktop/cea/rank/rank11-11/{}'.format(str(df)[2:-2]))
ninox = pd.read_csv('ninox.csv')



# Result file
result=pd.DataFrame(columns=['Title', 'Lead Owner', 'Industry', 'Phone', 'Age', 'Lead Source',
       'Lead Type', 'Sustainability/Green Design', 'Name', 'Lead First Name',
       'Lead Last Name', 'Primary Lead Email', 'Secondary Lead Email',
       'Website', 'Stage', 'No. Employees', 'Linkedin url', 'Street',
       'Country', 'Zip Code', 'City', 'State/Province', 'Description',
       'Property Address', 'Date of Last Link Clicked',
       'Date of Last Tracked View', 'Total Tracked Views'])


# Filter streak data
df1=df[(df['Stage']=='Contacted -I') | (df['Stage']=='Contacted - II') | (df['Stage']=='Contacted -III')]
df2=df1[df1['Total Tracked Views']>0]


# Append the data to result file
result['Name']=df2['Name']
result['Date of Last Tracked View']=df2['Date of Last Tracked View']
result['Total Tracked Views']=df2['Total Tracked Views']
result['Property Address']=df2['Property Address']
result['Date of Last Link Clicked']=df2['Date of Last Link Clicked']
result['Stage']=df2['Stage']

result['Title']='Alisha McFetridge'
result['Lead Owner']='Owner'
result['Industry']='Contractor/Builder'
result['Lead Source']='California CEA Pilot'
result['Lead Type']='potential bathroom Pro'
result['Country']='USA'



# Change column names for ninox data
ninox.columns=['Last Enhancement Date', 'Name of the Firm', 'Enhanced Business Name',
       'Address', 'City', 'State', 'Zip Code',
       'Contact Phone', 'Owner Email',
       'Owner First Name', 'Owner Last Name', 'Is this a GC?',
       'Owner Phone Number DIY',
       'Owner Email DIY', 'Owner Age',
       'Sustainability, Environment, Renewable, Green, Water Conservation Focus',
       'Company Website', '# Employees', 'LinkedIn URL (If exists)',
       'Company About Us Description', 'Website Rating',
       'Do they do Commercial Work', 'BuildZoom Profile Exists',
       'Years in Biz', 'LinkedIn Presence']


# Match with Name of the Firm
table1=pd.merge(result,ninox[['Name of the Firm', 'Enhanced Business Name','Address', 'City', 'State', 'Zip Code',
                            'Contact Phone', 'Owner Email','Owner Phone Number DIY','Owner Email DIY', 'Owner Age',
                            'Sustainability, Environment, Renewable, Green, Water Conservation Focus','Owner First Name', 'Owner Last Name',
                            'Company Website', '# Employees', 'LinkedIn URL (If exists)',
                            'Company About Us Description', 'Website Rating',
                            'Do they do Commercial Work', 'BuildZoom Profile Exists',
                            'Years in Biz', 'LinkedIn Presence']],left_on='Name',right_on='Name of the Firm',how='left')


# Keep those rows that are matched
table1_ = table1[table1['Name of the Firm'].notna()]



# ### Not Matched rows:

table1_na = table1[table1['Name of the Firm'].isna()]
table1_na_=table1_na_.drop_duplicates(subset=['Name'])
table1_na_1=table1_na_.iloc[:-1,:]


table1_na_1=table1_na_1.iloc[:,:27]


# Match with enhanced business name
table2 = pd.merge(table1_na_1,ninox[['Name of the Firm', 'Enhanced Business Name','Address', 'City', 'State', 'Zip Code',
                            'Contact Phone', 'Owner Email','Owner Phone Number DIY','Owner Email DIY', 'Owner Age',
                            'Sustainability, Environment, Renewable, Green, Water Conservation Focus','Owner First Name', 'Owner Last Name',
                            'Company Website', '# Employees', 'LinkedIn URL (If exists)',
                            'Company About Us Description', 'Website Rating',
                            'Do they do Commercial Work', 'BuildZoom Profile Exists',
                            'Years in Biz', 'LinkedIn Presence']],left_on='Name',right_on='Enhanced Business Name',how='left')


table2_clean=table2[table2['Name of the Firm'].notna()]


table2_=table2_clean.drop_duplicates(subset=['Enhanced Business Name'])



# ### Not Matched rows2:


table2_na = table2[table2['Enhanced Business Name'].isna()]



table2_na =table2_na.iloc[:,:27]


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


# Match with Name of the Firm
matcher.load_and_process_master_data('Name of the Firm', ninox)
match_table=matcher.match_names(to_be_matched=table2_na, column_matching='Name')



# Filter by score 70
match_table2 = match_table[ (match_table['score'] > 70) ]



# Merge match table with result table
table3=pd.merge(table2_na,match_table2[['original_name','match_name']],left_on='Name',right_on='original_name',how='left')


table3 = table3.drop('original_name', axis=1)



# Match with Name of the Firm
table3_=pd.merge(table3,ninox[['Name of the Firm', 'Enhanced Business Name','Address', 'City', 'State', 'Zip Code',
                            'Contact Phone', 'Owner Email','Owner Phone Number DIY','Owner Email DIY', 'Owner Age',
                            'Sustainability, Environment, Renewable, Green, Water Conservation Focus','Owner First Name', 'Owner Last Name',
                            'Company Website', '# Employees', 'LinkedIn URL (If exists)',
                            'Company About Us Description', 'Website Rating',
                            'Do they do Commercial Work', 'BuildZoom Profile Exists',
                            'Years in Biz', 'LinkedIn Presence']],left_on='match_name',right_on='Name of the Firm',how='left')



# Drop match_name column and keep the same columns
table3_ = table3_.drop('match_name', axis=1)


# ### Combine result


table1_=table1_.rename(columns={"Zip Code_y": "Zip Code", "City_y": "City"})

final_res = table1_.append([table2_, table3_])


final_res['Phone']=final_res['Owner Phone Number DIY']
final_res['Age']=final_res['Owner Age']
final_res['Sustainability/Green Design']=final_res['Sustainability, Environment, Renewable, Green, Water Conservation Focus']
final_res['Lead First Name']=final_res['Owner First Name']
final_res['Lead Last Name']=final_res['Owner Last Name']
final_res['Primary Lead Email']=final_res['Owner Email']
final_res['Secondary Lead Email']=final_res['Owner Email DIY']
final_res['Website']=final_res['Company Website']
final_res['No. Employees']=final_res['# Employees']
final_res['Linkedin url']=final_res['LinkedIn URL (If exists)']
final_res['Description']=final_res['Company About Us Description']
final_res['Street']=final_res['Address']
final_res['Zip Code_x']=final_res['Zip Code']
final_res['City_x']=final_res['City']
final_res['State/Province']=final_res['State']


final_res_=final_res.iloc[:,:27]


final_res_.to_excel('open_data.xlsx')
