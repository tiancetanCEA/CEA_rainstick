import pandas as pd 
import re
import numpy as np
from itertools import chain
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
from itertools import chain
import gspread
import hashlib
import geocoder 
import json
from gspread_dataframe import set_with_dataframe

gc = gspread.service_account("credentials.json")

spreadsheet2 = gc.open_by_url("https://docs.google.com/spreadsheets/d/1uy2ICzAOxxLv-Lm5AaihAy2UYPDCiq0sePNUvNdIOvY/edit?sharingaction=ownershiptransfer#gid=0")
worksheet = spreadsheet2.get_worksheet(2)
data2 = worksheet.get_all_values()
df_masterfile=pd.DataFrame(data2)
df_masterfile.columns = df_masterfile.iloc[0]
df_masterfile = df_masterfile.iloc[1:]
df1=df_masterfile


# Fill empty Enhanced Business Name
df1=df1.mask(df1 == '')
df1['Enhanced Business Name']=df1['Enhanced Business Name'].fillna(df1['Firm Name'])

df=df1.copy()


# 1. Data Cleaning & Transformations
	# 1. remove extra space
	# 2. remove punctuation
	# 3. remove website link from Generic Company Contact Email
	# 4. remove unrelated text from address, city, Owner Email, Owner name
	# 4. Missing value in zip code, but address is not empty. Fill in Zip code.(Python package: geocode)
	# 5. transform phone numbers to a default format
# 2. Flag rules.
	# has LinkedIn Presence, NO LinkedIn URL
	# has BuildZoom Profile, NO BuildZoom Score
	# has website, NO website rating
	# No website, has website rating
	# has FB presence, NO Facebook URL
	# has Instagram Presence, NO Instagram URL
	# Firm on Blue Book , NO Blue Book URL
	# High Website rating score, Low other scores?

#FLAG
df['LinkedIn URL (If exists)'] = df['LinkedIn URL (If exists)'].replace(np.nan, -1)
df['BuildZoom Score (If Exists)'] = df['BuildZoom Score (If Exists)'].replace(np.nan, -1)
df['Online Reviews on Buildzoom'] = df['Online Reviews on Buildzoom'].replace(np.nan, -1)
df['Facebook URL(if exists)'] = df['Facebook URL(if exists)'].replace(np.nan, -1)
df['Instagram URL(If exists)'] = df['Instagram URL(If exists)'].replace(np.nan, -1)
df['Blue book URL'] = df['Blue book URL'].replace(np.nan, -1)


df['flag1'] = ['LinkedIn Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['LinkedIn Presence'],df['LinkedIn URL (If exists)'])]
df['flag2'] = ['BuildZoom Profile Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['BuildZoom Profile Exists'],df['BuildZoom Score (If Exists)'])]
# df['flag3'] = ['BuildZoom Profile Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['BuildZoom Profile Exists'],df['Online Reviews on Buildzoom'])]
df['flag4'] = ['FB Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['FB Presence'],df['Facebook URL(if exists)'])]
df['flag5'] = ['Instagram Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['Instagram Presence'],df['Instagram URL(If exists)'])]
df['flag6'] = ['Blue Book Incomplete' if i == 'Yes' and j == -1 else '' for i,j in zip(df['Is firm on Blue Book?'],df['Blue book URL'])]


df['Company Website'] = df['Company Website'].replace(np.nan, -1)
df['Company Website'] = np.where(df['Company Website'].str.startswith("http://no"), -1, df['Company Website'])
df['Website Rating'] = df['Website Rating'].replace(np.nan, -1)
df['flag7'] = ['Company Website Incomplete' if i == -1 and j != -1 else '' for i,j in zip(df['Company Website'],df['Website Rating'])]
df['flag8'] = ['Company Website Incomplete' if i != -1 and j == -1 else '' for i,j in zip(df['Company Website'],df['Website Rating'])]

def combine_cells(row):
    values = [str(row['flag1']), str(row['flag2']), str(row['flag4']), str(row['flag5']), str(row['flag6']), str(row['flag7']), str(row['flag8'])]
    values = [val for val in values if pd.notna(val)]
    return ' '.join(values)

# apply the function to the entire dataframe
df['flag'] = df.apply(combine_cells, axis=1)

df2=df.drop(columns=['flag1','flag2','flag4', 'flag5','flag6', 'flag7','flag8'])
df2=df2['flag']

df3=pd.merge(df1,df2, left_index=True, right_index=True)


# Data cleaning and transformation
df3=df3.mask(df3 == '')
df3 = df3.applymap(lambda x: x.strip(' ') if type(x) == str else x)

df3['Generic Company Contact Email']=df3['Generic Company Contact Email'].str.replace(r'(https?://\S+)', '')
df3['Owner Phone Number'] = df3['Owner Phone Number'].str.replace('[^\d]+', '')
df3['Owner Email']=df3['Owner Email'].str.replace(r'(https?://\S+)', '')
df3['Owner Email'] = df3['Owner Email'].where(pd.notnull(df3['Owner Email']), '').astype(str)
df3['Owner Email'] = df3['Owner Email'].str.replace(r'\d{3}-\d{3}-\d{4}', '')
df3['Owner Email'] = df3['Owner Email'].str.replace(r'\(\d{3}\)\s\d{3}-\d{4}', '')
df3['Owner Email'] = df3['Owner Email'].str.replace(r'\d{10}', '')
df3['Owner Email']  = df3['Owner Email'] .str.replace(r'\b\d{3}\.\d{3}\.\d{4}\b', '')
df3['Owner Email'] = df3['Owner Email'].where(df3['Owner Email'].astype(str).str.len() <= 100, None)
df3['Generic Company Contact Email'] = df3['Generic Company Contact Email'].where(df3['Generic Company Contact Email'].astype(str).str.len() <= 100, None)
df3['Owner First Name'] = df3['Owner First Name'].where(df3['Owner First Name'].astype(str).str.len() <= 30, None)
df3['Owner Last Name'] = df3['Owner Last Name'].where(df3['Owner Last Name'].astype(str).str.len() <= 30, None)

df3['Owner First Name'] = df3['Owner First Name'].str.replace('[^\w\s]', '')
df3['Owner Last Name'] = df3['Owner Last Name'].str.replace('[^\w\s]', '')
df3["Owner First Name"] = df3["Owner First Name"].str.title()
df3["Owner Last Name"] = df3["Owner Last Name"].str.title()
df3["City"] = df3["City"].str.title()

df3["Address"] = df3["Address"].str.replace(":","", regex=False)
df3["Address"] = df3["Address"].str.replace(";","", regex=False)
df3["Address"] = df3["Address"].str.replace("'","", regex=False)
df3["Address"] = df3["Address"].str.title()

df3=df3.mask(df3 == '')

# create unique keys based on business name 
z = np.empty((0, 2))
bn = df3['Enhanced Business Name'].unique() 

for row in bn:
    y = hashlib.sha1(json.dumps(row).encode()).hexdigest()
    z = np.append(z,np.array([[row, y]]), axis = 0 )
    z = pd.DataFrame(z, columns = ['Enhanced Business Name','Business_ID'])

df3 = df3.merge(z)

# Uncomment to send data to the google sheet
worksheet.clear() 
set_with_dataframe(worksheet, df3) 

worksheet.unmerge_cells('A1:AW4398')



