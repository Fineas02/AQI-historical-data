import pandas as pd
import matplotlib.pyplot as plt

# Base directory and file names
base_dir = '/Users/fineas/Desktop/Coding/AQI_Proj/county_csv/'
file_names = [
   'daily_aqi_by_county_2008.csv',
    'daily_aqi_by_county_2009.csv',
    'daily_aqi_by_county_2010.csv',
    'daily_aqi_by_county_2011.csv',
    'daily_aqi_by_county_2012.csv',
    'daily_aqi_by_county_2013.csv',
    'daily_aqi_by_county_2014.csv',
    'daily_aqi_by_county_2015.csv',
    'daily_aqi_by_county_2016.csv',
    'daily_aqi_by_county_2017.csv',
    'daily_aqi_by_county_2018.csv',
    'daily_aqi_by_county_2019.csv',
    'daily_aqi_by_county_2020.csv',
    'daily_aqi_by_county_2021.csv',
    'daily_aqi_by_county_2022.csv',]

# Generate a list of file paths
file_paths = [base_dir + file_name for file_name in file_names]

# Read each CSV file into a DataFrame and concatenate them together
df_county = pd.concat([pd.read_csv(file_path) for file_path in file_paths])

# Convert the 'Date' column to datetime
df_county['Date'] = pd.to_datetime(df_county['Date'])

# Specify the county you're interested in
county_of_interest = 'Rockland'

# Filter the county dataframe for the specified county
county_data = df_county[df_county['county Name'] == county_of_interest].copy()

# Compute the weekly average AQI
county_data['YearWeek'] = county_data['Date'].dt.to_period('W')  # create a new column with the year and week
weekly_avg_aqi = county_data.groupby('YearWeek')['AQI'].mean()  # compute the weekly average AQI

# Convert the index to datetime format for plotting
weekly_avg_aqi.index = weekly_avg_aqi.index.to_timestamp()

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create a bar plot of the weekly average AQI
ax.bar(weekly_avg_aqi.index, weekly_avg_aqi, color='blue', label='Weekly Average AQI')

# Add horizontal lines for the AQI thresholds at 50 and 100
ax.axhline(0, color='green', linestyle='--', label='Good (0)')
ax.axhline(50, color='orange', linestyle='--', label='Moderate (50)')
ax.axhline(100, color='red', linestyle='--', label='Moderate/Unhealthy for Sensitive Groups (100)')

# Set the title and labels
ax.set_title(f'Weekly Average AQI for {county_of_interest} County')
ax.set_ylabel('AQI')
ax.set_xlabel('Date')

# Add a legend
ax.legend()

# Automatically adjust the subplot layout
fig.tight_layout()

# Display the plot
plt.show()
