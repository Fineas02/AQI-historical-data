import json
import pandas as pd
import plotly.graph_objects as go

# Load the data file
with open('/Users/fineas/Desktop/Coding/AQI_Proj/test.json') as f:
    data = json.load(f)

# Manually parse the JSON data into a list of dictionaries
data_list = [{'county': entry['county'], 'date_local': entry['date_local'], 'aqi': entry['aqi'], 'arithmetic_mean': entry['arithmetic_mean']} for entry in data]

# Convert the data list to a DataFrame
df = pd.DataFrame(data_list)

# Convert 'date_local' to datetime format
df['date_local'] = pd.to_datetime(df['date_local'])

# Keep only the rows with the maximum 'aqi' for each county for each day
df_max_aqi = df.loc[df.groupby(['county', 'date_local'])['aqi'].idxmax()]

# Get the list of unique counties
counties = df_max_aqi['county'].unique()

# For each county, create a chart and save it as an HTML file
for county in counties:
    # Create a DataFrame for this county
    county_df = df_max_aqi[df_max_aqi['county'] == county]
    
    # Create a line for AQI
    trace_aqi = go.Scatter(
        x=county_df['date_local'],
        y=county_df['aqi'],
        name='AQI',
        hovertemplate='AQI: %{y}<extra></extra>'
    )

    # Create a line for PM2.5
    trace_pm25 = go.Scatter(
        x=county_df['date_local'],
        y=county_df['arithmetic_mean'],
        name='PM2.5',
        hovertemplate='PM2.5: %{y}<extra></extra>'
    )

    # Create a layout
    layout = go.Layout(
        title=f'AQI and PM2.5 over time for {county} County',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Value'),
        hovermode='x'
    )

    # Create a Figure and add the traces
    fig = go.Figure(data=[trace_aqi, trace_pm25], layout=layout)

    # Save the figure as an HTML file
    fig.write_html(f'/Users/fineas/Desktop/Coding/AQI_Proj/{county}_chart.html')
