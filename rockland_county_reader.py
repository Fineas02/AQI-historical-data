import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
df_county = pd.read_csv('/Users/fineas/Desktop/Coding/AQI_Proj/daily_aqi_by_county_2022.csv')

# Convert the 'Date' column to datetime
df_county['Date'] = pd.to_datetime(df_county['Date'])

# Specify the county you're interested in
county_of_interest = 'Rockland'

# Filter the county dataframe for the specified county
county_data = df_county[df_county['county Name'] == county_of_interest]

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the AQI data for the county
ax.plot(county_data['Date'], county_data['AQI'])
ax.set_title(f'AQI for {county_of_interest} County')
ax.set_ylabel('AQI')
ax.set_xlabel('Date')

# Automatically adjust the subplot layout
fig.tight_layout()
plt.show()
