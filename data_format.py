import geopandas as gpd
import matplotlib.pyplot as plt
import json
import pandas as pd

# Load JSON data
with open('/Users/fineas/Desktop/Coding/AQI_Proj/test.json') as f:
    data = json.load(f)

# Convert JSON data to pandas DataFrame
df = pd.json_normalize(data['Data'])

# Display the DataFrame
df.head()
# Load the NY state boundary file (a GeoJSON or shapefile)
ny = gpd.read_file('/Users/fineas/Desktop/Coding/AQI_Proj/tl_rd22_36_cousub/tl_rd22_36_cousub.shp')

# Set up the plot
fig, ax = plt.subplots()

# Plot the state boundary
ny.boundary.plot(ax=ax, color='black')

# Add data points from DataFrame
for i, row in df.iterrows():
    ax.scatter(row['longitude'], row['latitude'], c=row['aqi'], alpha=0.5, cmap='viridis')
    ax.text(row['longitude'], row['latitude'], f"AQI: {row['aqi']}\nMin: {row['first_max_value']}\nMax: {row['arithmetic_mean']}", fontsize=8)

plt.show()