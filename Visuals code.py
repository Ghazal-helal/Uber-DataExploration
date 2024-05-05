#all the necessary imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.express as px


weather= pd.read_csv('DE-dataset.csv',parse_dates=['Date'])


#Figure 1.1 Scatter plot change of temperature over the years 2009-2011
weather['DATE'] = pd.to_datetime(weather['DATE'])
plt.figure(figsize=(20, 5))
plt.scatter(weather['DATE'], weather['TEMP'], c=weather['TEMP'], cmap='winter_r', alpha=0.5)
plt.colorbar(label='TEMP')
plt.xlabel('Date')
plt.xlim(pd.to_datetime('2009-1-1'), pd.to_datetime('2011-12-30'))
plt.ylabel('Temperature')
plt.title('The Change of Temperature over the years')
plt.xticks(rotation=0)
plt.show()

#Figure 1.2 Scatter plot change of temperature over the years 20-201
weather['DATE'] = pd.to_datetime(weather['DATE'])
plt.figure(figsize=(20, 5))
plt.scatter(weather['DATE'], weather['TEMP'], c=weather['TEMP'], cmap='winter_r', alpha=0.5)
plt.colorbar(label='TEMP')
plt.xlabel('D1ate')
plt.xlim(pd.to_datetime('2012-1-1'), pd.to_datetime('2015-6-30'))
plt.ylabel('Temperature')
plt.title('The Change of Temperature over the years')
plt.xticks(rotation=0)
plt.show()

#Figure 1.3
'''Heatmap of Correlations:
Create a heatmap to visualize the correlations between various numerical columns in the dataset (e.g., temperature, wind speed, visibility).
This will help identify any significant relationships among the variables.
Python code using Seaborn:'''

plt.figure(figsize=(8, 6))
correlation = weather[['TEMP', 'WDSP', 'VISIB', 'MAX', 'MIN']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

#Figure 1.4
'''Heatmap of Correlations:
Create a heatmap to visualize the correlations between various numerical columns in the whole dataset
This will help identify any significant relationships among the variables.
Python code using Seaborn:'''
plt.figure(figsize=(8, 6))
correlation = weather[['TEMP', 'WDSP', 'VISIB', 'MAX', 'MIN','fare_amount','passenger_count']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


#Figure 1.5 a pair rid to highlight the different positive and negative relations in the dataset

weather_cols = ['DATE', 'TEMP', 'fare_amount', 'MAX', 'MIN', 'passenger_count']
DE_dataset = weather[weather_cols].copy()
scatter_matrix = pd.plotting.scatter_matrix(
    df_subset,
    figsize=(16, 16),
    diagonal='kde',
    alpha=0.5
)
for ax in scatter_matrix.flatten():
    ax.xaxis.label.set_rotation(0)
    ax.yaxis.label.set_rotation(0)
    ax.yaxis.label.set_ha('right')
plt.tight_layout()
plt.show()

#Figure 1.6 Scatter with the relation of the fare amount and passenger count over the years
weather['DATE'] = pd.to_datetime(weather['DATE'])


plt.figure(figsize=(15, 8))
plt.scatter(weather['DATE'], weather['fare_amount'], c=weather['passenger_count'], cmap='winter_r', alpha=0.5)

plt.colorbar(label='passenger_count')
plt.xlabel('Date')
plt.xlim(pd.to_datetime('2011-12-1'), pd.to_datetime('2014-03-1'))
plt.ylabel('Fare Amount')
plt.title('Connection between DATE and Fare Amount')
plt.xticks(rotation=0)
plt.show()

#Figure 1.7 showing the density of the fare amount compared with temperature
DE_dataset = {
    'fare_amount': [10, 15, 20, 25, 30, 35, 40, 45, 50],
    'TEMP': [15, 18, 20, 22, 25, 28, 30, 32, 35]
}
weather = pd.DataFrame(DE_dataset)
fare_amount = weather['fare_amount']
temperature = weather['TEMP']
plt.figure(figsize=(8, 6))
sns.kdeplot(fare_amount, fill=True, label='Fare Amount')
sns.kdeplot(temperature, fill=True, label='Temperature')
plt.xlabel('Value')
plt.ylabel('Density')
plt.xlim(-18,100)
plt.title('Overlapping Density Plot: Fare Amount vs Temperature')
plt.legend()
plt.show()

#Figure 1.8 Scatter with the relation of the fare amount and passenger count over the temperature
fare_amount_limit = 900
passenger_count_limit = 900
filtered_data = weather[(weather['fare_amount'] <= fare_amount_limit) &
                           (weather['passenger_count'] <= passenger_count_limit)]
fare_amount = filtered_data['fare_amount']
passenger_count = filtered_data['passenger_count']
temperature = filtered_data['TEMP']
fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(fare_amount, passenger_count, c=temperature, cmap='coolwarm')
ax.set_xlabel('Fare Amount')
ax.set_ylabel('Passenger Count')
ax.set_title('Dot Plot: Fare Amount vs. Passenger Count')
cbar = plt.colorbar(sc)
cbar.set_label('Temperature')
plt.show()


#Figure 1.9 Map based on the temp of the uber rides locations
fig = px.scatter_geo(weather,
                     lon = weather['pickup_latitude'],
                     lat = weather['pickup_longitude'],
                     color='TEMP')

fig.update_layout(
        title = 'Number of Uber rides Mapped on Location Based on Temperature',
        geo_scope='usa', height=500
    )
fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True, visible=False, resolution=50,
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Black")

fig.update_geos(
    lataxis_showgrid=True, lonaxis_showgrid=True
)
fig.show()
#Figure 1.10 The Weather Stations Mapped on Location Based on the Station Pressure
fig = px.scatter_geo(weather,
                     lon = weather['LONGITUDE'],
                     lat = weather['LATITUDE'],
                     size='STP',
                     color="STP",
                     labels={"station pressure": "STP"}
                     )

fig.update_layout(
        title = 'The Weather Stations Mapped on Location Based on the Station Pressure',
        geo_scope='usa', height=500,
        showlegend=True
      )
fig.update_layout(showlegend=True,legend_bordercolor="#444")

fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True, visible=False, resolution=50,
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Black",
                center_lat=42.3647,
                center_lon =-71.0542
)
fig.show()

#Figure 1.11 scatter of the stations based on the name and the fare amount over the years in the data
sns.catplot(data=weather, x='Date', y='fare_amount',
    hue='NAME', height=6, aspect=10/6)
plt.show()

sns.catplot(data=weather, x='Date', y='NAME',
    hue='NAME', height=6, aspect=10/6)
plt.show()

#Figure 1.12 line plot of three variables in the dataset
plt.plot(weather['Date'], weather['TEMP'], label = " fare_amount", linestyle="--")
plt.plot(weather['Date'], weather['TEMP'], label = " WDSP", linestyle="-.")
plt.plot(weather['Date'], weather['TEMP'], label = "VISIB ", linestyle=":")
plt.xlim(pd.to_datetime('2014-1-1'), pd.to_datetime('2014-12-30'))
plt.legend()
plt.show()

#Figure 1.13 line plot the fare amount over the years
plt.figure(figsize=(15,10))
plt.plot(weather['Date'], weather['fare_amount'], label = "fare", linestyle="solid")
plt.xlim(pd.to_datetime('2014-1-1'), pd.to_datetime('2014-12-30'))
plt.title("The Change of the Uber fares through each day for the whole year")
plt.legend()
plt.show()

