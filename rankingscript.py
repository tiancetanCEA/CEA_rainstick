#!/usr/bin/env python
# coding: utf-8

import os
os.getcwd()
os.chdir('/Users/apple/Desktop/cea/rank/rank11-11') 
import pandas as pd
import numpy as np 

zip_data  = pd.read_excel(io = 'permit_zip_code_MSA.xlsx', sheet_name = 'Sheet1')
rainstick_open_data = pd.read_excel(io = 'streak_export_data.xlsx', sheet_name = 'Sheet1')
# rainstick_ninox_data = pd.read_excel(io = 'GCRemodeler Firm Profiling (4).xlsx', sheet_name = 'GCRemodeler Firm Profiling (4)')
rainstick_ninox_data = pd.read_csv('ninox.csv')


zip_data=zip_data.dropna()



def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


rainstick_ninox_data['Owner Age'] = rainstick_ninox_data['Owner Age']*-1
rainstick_ninox_data['Owner_age_scaled'] = NormalizeData(rainstick_ninox_data['Owner Age'])



ss_array = np.empty((0,10))

for bn, row1, row2, row3, row4, row5, row6, row7, row8 in rainstick_ninox_data[['Name of the Firm','Do they do Commercial Work', '# Employees',  'Years in Biz',  'Owner_age_scaled', 'BuildZoom Profile Exists', 'LinkedIn Presence', 'Website Rating', 'Sustainability, Environment, Renewable, Green, Water Conservation Focus']].itertuples(index=False) :
    f1, f2,f3,f4,f5, f5b, f6, f7,f8 = 0,0,0,0,0,0,0,0,0
    #1. Commercial Work
    if row1 == 'Yes' :
        f1 = 5
    elif row1 == 'No':
        f1 = 0
    else :
        f1 = 0 
    
    #2. # Employees
    if row2 == '20+' :
        f2 = 5
    elif row2 == '10 to 20':
        f2 = 3
    elif row3 == '5 to 10':
        f2 = 2
    elif row3 == '0 to 5':
        f2 = 1
    else :
        f2 = 0

    #3. years in biz
    if row3 == '15+' :
        f3 = 5
    elif row3 == '10 to 15':
        f3 = 3
    elif row3 == '5 to 10':
        f3 = 2
    elif row3 == '0 to 5':
        f3 = 1
    else :
        f3 = 0
        
    #4.Owner's Age
    if row4 > 0  :
        f5 = row4*5
    else:
        f5 = 0
    
    #5. BUILDZOOM PROFILE
    if row5  == 'Yes' :
        f5 = 5
    elif row5 == 'No':
        f5 = 0
    
    #6. LINKEDIN PRESENCE
    if row6  == 'Yes' :
        f6 = 5
    elif row6 == 'No':
        f6 = 0
    
    #7. WEBSITE RATING 

    if row7 == '4 - Sophisticated Website, high quality, reviews' :
        f7 = 5
    elif row7 == '3 - Beyond Basic with design and detailed project info':
        f7 = 3
    elif row7 == '2 - Basic design, few projects ':
        f7 = 2
    elif row7 == '1 - Poor, rudimentary website ':
        f7 = 1
    else :
        f7 = 1
    #8. Green
    if row8  == 'Yes' :
        f8 = 5
    elif row8 == 'No':
        f8 = 0
    


    ss = .2*f1 + .1*f2 + .1*f3 + .1*f4 + .25*f5 + .1*f5b +.1*f6 +.2*f7 + .25*f8 
    ss_array = np.append(ss_array, np.array([[bn, f1, f2,f3,f4,f5,f6, f7, f8,ss]]), axis = 0 )
    



ss_array =  pd.DataFrame(ss_array, columns = ['Name of the Firm', 'Score: Commercial Work', 
                                              'Score: # Employees',  'Score: Years in Biz',
                                              'Score: Owner Age','Score: BuildZoom Profile Exists Score',
                                              'Score: LinkedIn Presence','Score: Website Rating',
                                              'Score: Green','Size and Stability Score'])



ss_array['Size and Stability Score'] = ss_array['Size and Stability Score'].astype(float)

ss_array['Size and Stability Score'] = NormalizeData(ss_array['Size and Stability Score'])



ss_array[ss_array['Name of the Firm']=='Teichert Construction']



zip_data=zip_data.drop_duplicates()



df1=pd.merge(rainstick_ninox_data,zip_data,left_on='Zip Code',right_on='PROPERTYADDRESSZIP',how='left')



df1=df1.drop_duplicates()


df1['If_SF'] = df1['COMBINEDSTATISTICALAREA']=='San Jose-San Francisco-Oakland, CA'



df2=pd.merge(rainstick_open_data,ss_array,left_on='Name',right_on='Name of the Firm',how='left')

df1=df1.iloc[:,[1,-1]]



df3=pd.merge(df2,df1,left_on='Name',right_on='Name of the Firm',how='left')


df3=df3.drop(columns=['Name of the Firm_x', 'Score: Commercial Work',
       'Score: # Employees', 'Score: Years in Biz', 'Score: Owner Age',
       'Score: BuildZoom Profile Exists Score', 'Score: LinkedIn Presence',
       'Score: Website Rating', 'Score: Green', 'Name of the Firm_y',])


df3 =df3.replace({'If_SF': {True: 'Yes', False: 'No'}})


df3=df3.drop_duplicates()


df3.to_excel('output_new1.xlsx')
