#The Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno

#Open the uber and NOAA dataset
uber= pd.read_csv('uber_daily.csv',parse_dates=['key'])
weather= pd.read_csv('weather.csv',parse_dates=['DATE'])

#Changing columns name to merge the datasets
df1=pd.DataFrame(uber)
df1.rename(columns={'key': 'DATE',
'Unnamed: 0': 'Trip_ID'},inplace=True)

#Saving changes to new csv file
df2=pd.DataFrame(weather)
Final=pd.merge(uber,weather)
Final.to_csv('Merged.csv')

#Open file and change Date&Time to Date only to new column
Merged= pd.read_csv('Merged.csv',parse_dates=['DATE'])
df=pd.DataFrame(Merged)
df['DATE'] = pd.to_datetime(df['DATE'])
df['Date'] = df['DATE'].dt.date

#First step of cleaning - Exploring
print(Merged.info())
print(Merged.duplicated().sum())
print(Merged.isnull().sum())

#Checking for missing values
msno.bar(Merged)
plt.show()

msno.heatmap(Merged)
plt.show()

#Replacing the nan 999.9 values with the average
df['DEWP'] = df['DEWP'].replace([9999.9], 42.6)
df['SLP'] = df['SLP'].replace([9999.9], 1013)
df['STP'] = np.where(df['STP'] > 100, 13.7, df['STP'])
df['MXSPD'] = df['MXSPD'].replace([999.9],11.1)
df['GUST'] = df['GUST'].replace([999.9], 27.3)
print(Merged['PRCP'].describe())

#The snow depth is empty so we drop the column
df.drop('SNDP' ,inplace=True,axis=1)

#The clean file
df.to_csv('DE-dataset.csv')


Merged= pd.read_csv('DE-dataset.csv',parse_dates=['Dشفث'])
df1=pd.DataFrame(Merged)
df1.rename(columns={'key': 'DATE',},inplace=True)