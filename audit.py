#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import numpy as np 
os.chdir('/Users/apple/Desktop/cea/auditscript') 


# 6.  Quality control checks														
# 	!Building types, if lite commercial only, should not have single family homes or residential in website text = flag for audit													
# 	!High IG or FB scores and low website rating, flag for check					0-1	0.8		fb/yes					
# 	!High SEO rank (near top of list), but poor website					0-1								
# 	Check on luxury score and website scrape for premium, design, luxury						0-1	<.5 + kw						
# 	!Data completeness (if they have Buildzoom account, must have score etc)							bzscore						


df=pd.read_csv('Stone Masons.csv')



def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


# - Building types, if lite commercial only, should not have single family homes or residential in website text = flag for audit


#Combine all website text data
df['ALL TEXT'] = df['Text Capture 1: About us or General Description'] + df['Text Capture 2: Description of Services'] + df['Text Capture 3: Customer testimonials or reviews'] + df['Text Capture 4: Other']
df['ALL TEXT'] = df['ALL TEXT'].astype(str)
df['ALL TEXT'] = df['ALL TEXT'].replace('\n','', regex=True)



# Create a column named flag_building_types
# Return Yes if meet condition
df['flag1'] = ['Check Building Types' if i=='Lite Commercial' and ("single family homes" in j or "residential" in j) else '' for i,j in zip(df['Building types covered'],df['ALL TEXT'])]


# - High IG or FB scores and low website rating, flag for check

# Replace category variables to 1-6 / 0-1
df['Total IG Posts'].replace(['500+','101-500','51-100','11-50','<10','0'],
                        [6,5,4,3,2,1], inplace=True)
df['Total FB Posts'].replace(['100+','51-100','21-50','6-20','1-5','0'],
                        [6,5,4,3,2,1], inplace=True)
df['Website Rating'].replace(['1 - Poor, rudimentary website ','2 - Basic design, few projects ','3 - Beyond Basic with design and detailed project info','4 - Sophisticated Website, high quality, reviews'],
                        [0.25,0.5,0.75,1], inplace=True)



# IF webscore is 1-poor rudmentary website and total IG/FB posts are high
# Then we flag it
df['flag2'] = ['High IG / Low Webscore' if k ==0.25 and (i > 4 or j > 4) else '' for i,j,k in zip(df['Total IG Posts'],df['Total FB Posts'],df['Website Rating'])]


# - High SEO rank (near top of list), but poor website


df['SEO Rank'].replace(['Top 10', 'Top 20', 'Top 30', 'Top 50','"Outside Top 50 "','Top 10, "Outside Top 50 "'],
                        [1,0.75,0.5,0.25,0,0], inplace=True)



df['flag3'] = ['Check SEO rank / Webscore' if i == 1 and j == 0.25 else '' for i,j in zip(df['SEO Rank'],df['Website Rating'])]


# - Data completeness (if they have Buildzoom account, must have score etc)

# Replace nan values to -1
df['BuildZoom Score (If Exists)'] = df['BuildZoom Score (If Exists)'].replace(np.nan, -1)
df['Facebook URL(if exists)'] = df['Facebook URL(if exists)'].replace(np.nan, -1)
df['Instagram URL(If exists)'] = df['Instagram URL(If exists)'].replace(np.nan, -1)
df['Is firm on Blue Book?'] = df['Is firm on Blue Book?'].replace(np.nan, -1)
df['Total IG Posts'] = df['Total IG Posts'].replace(np.nan, -1)
df['Total FB Posts'] = df['Total FB Posts'].replace(np.nan, -1)


df['flag4'] = ['Buildzoom Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['BuildZoom Profile Exists'],df['BuildZoom Score (If Exists)'])]
df['flag5'] = ['IG Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['Instagram Presence'],df['Instagram URL(If exists)'])]
df['flag6'] = ['FB Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['FB Presence'],df['Facebook URL(if exists)'])]
df['flag7'] = ['Bluebook Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['Is firm on Blue Book?'],df['Blue book URL'])]



df['flag9'] = ['IG Total Posts Incomplete' if i == 'Yes' and j ==-1 else '' for i,j in zip(df['Instagram Presence'],df['Total IG Posts'])]
df['flag10'] = ['FB Total Posts Incomplete' if i == 'Yes' and j ==-1 else '' for i,j in zip(df['FB Presence'],df['Total FB Posts'])]





# - Check on luxury score and website scrape for premium, design, luxury 0-1 <.5 + kw


# Normalize Luxury Project Score
df['Luxury Project Score']=NormalizeData(df['Luxury Project Score'])


df['flag8'] = ['Check Luxury Score / web text' if i < 0.51 and ("premium" in j or "design" in j or "luxury" in j) else '' for i,j in zip(df['Luxury Project Score'],df['ALL TEXT'])]



df['flag']=df['flag1']+' '+df['flag2']+' ' +df['flag3']+' ' +df['flag4']+' ' +df['flag5']+' ' +df['flag6']+' ' +df['flag7']+' ' +df['flag8']+' ' +df['flag9']+' ' +df['flag10']


df1=df.drop(columns=['ALL TEXT', 'flag1',
       'flag2', 'flag3','flag4', 'flag5',
       'flag6', 'flag7','flag8','flag9','flag10'])




df1.to_excel('result.xlsx')

