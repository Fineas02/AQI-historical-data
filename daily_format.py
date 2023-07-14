import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
df = pd.read_csv('/Users/fineas/Desktop/Coding/AQI_Proj/daily_aqi_by_cbsa_2022.csv')
df_county = pd.read_csv('/Users/fineas/Desktop/Coding/AQI_Proj/daily_aqi_by_county_2022.csv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df_county['Date'] = pd.to_datetime(df_county['Date'])

# Select the first CBSA and County from the data
first_cbsa = df['CBSA'].iloc[0]
first_county = df_county['county Name'].iloc[0]

# Filter the data for the first CBSA and County
cbsa_data = df[df['CBSA'] == first_cbsa]
county_data = df_county[df_county['county Name'] == first_county]

# Create a figure with two subplots
fig, axs = plt.subplots(2, figsize=(10, 8))

# Plot the AQI data for the first CBSA
axs[0].plot(cbsa_data['Date'], cbsa_data['AQI'])
axs[0].set_title(f'AQI for {first_cbsa}')
axs[0].set_ylabel('AQI')
axs[0].set_xlabel('Date')

# Plot the AQI data for the first County
axs[1].plot(county_data['Date'], county_data['AQI'])
axs[1].set_title(f'AQI for {first_county} County')
axs[1].set_ylabel('AQI')
axs[1].set_xlabel('Date')

# Automatically adjust the subplot layout
fig.tight_layout()
plt.show()
