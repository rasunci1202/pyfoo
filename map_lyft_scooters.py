import numpy
import matplotlib.pyplot as plt
import requests
import json
import pandas
import geopandas as gpd
import pyproj
import fiona
from shapely.geometry import Point, Polygon

my_lacounty_shapefile = 'c:/Users/bisuser/Downloads/DPW_CITY_BOUNDARIES/DPW_CITY_BOUNDARIES.shp'
my_lacounty_gdf = gpd.read_file(my_lacounty_shapefile)

my_fig = plt.figure(figsize=(16, 10), tight_layout=True)
my_ax = my_fig.add_subplot()
my_ax.set_xlim(6350000, 6650000)
my_ax.set_ylim(1550000, 1900000)
my_lacounty_gdf.plot(ax=my_ax, color='orange', edgecolor='black')

my_url = 'https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json'
my_file = 'c:/Users/bisuser/Documents/free_bike_status.json'
my_lyft_data = ''
my_lyft_locs = []

if (True):
    my_r = requests.get(my_url)
    if my_r.status_code == 200:
        my_lyft_data = my_r.json()
    else:
        print('error handler here')
else:
    with open(my_file) as my_fh:
        my_json = my_fh.read()
    my_lyft_data = json.loads(my_json)

#print(my_lyft_data['data']['bikes'][0])

my_lyft_bikes = my_lyft_data['data']['bikes']
for i in range(10):
    my_bike = my_lyft_bikes[i]['bike_id']
    my_lon = my_lyft_bikes[i]['lon']
    my_lat = my_lyft_bikes[i]['lat']
    my_lyft_locs.append([my_bike, my_lon, my_lat])

#print(my_lyft_locs[0])

my_lyft_df = pandas.DataFrame(my_lyft_bikes)
#print(my_lyft_df.shape)
my_lyft_geom = [Point(lon, lat) for lon, lat in zip(my_lyft_df['lon'], my_lyft_df['lat'])]
my_lyft_geom_df = pandas.DataFrame(my_lyft_geom, columns=['geometry'])
#print(my_lyft_geom_df.shape)
my_lyft_gis_df = my_lyft_df.join(my_lyft_geom_df)
my_lyft_gpd = gpd.GeoDataFrame(my_lyft_gis_df, crs={'init':'epsg:4326'})
#print(my_lyft_gpd)

my_lyft_gpd['geometry'] = my_lyft_gpd['geometry'].to_crs(epsg=2229)
my_lyft_gpd.plot(ax=my_ax, color='green')

plt.show()
