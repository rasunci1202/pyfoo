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

my_url = 'https://mds.bird.co/gbfs/los-angeles/free_bikes'
my_file = 'c:/Users/bisuser/Documents/bird/free_bikes.json'
my_bird_data = ''
my_bird_locs = []

if (True):
    my_r = requests.get(my_url)
    if my_r.status_code == 200:
        my_bird_data = my_r.json()
    else:
        print('error handler here')
else:
    with open(my_file) as my_fh:
        my_json = my_fh.read()
    my_bird_data = json.loads(my_json)

my_bird_bikes = my_bird_data['data']['bikes']
for i in range(10):
    my_bike = my_bird_bikes[i]['bike_id']
    my_lon = my_bird_bikes[i]['lon']
    my_lat = my_bird_bikes[i]['lat']
    my_bird_locs.append([my_bike, my_lon, my_lat])

my_bird_df = pandas.DataFrame(my_bird_bikes)
my_bird_geom = [Point(lon, lat) for lon, lat in zip(my_bird_df['lon'], my_bird_df['lat'])]
my_bird_geom_df = pandas.DataFrame(my_bird_geom, columns=['geometry'])
my_bird_gis_df = my_bird_df.join(my_bird_geom_df)
my_bird_gpd = gpd.GeoDataFrame(my_bird_gis_df, crs={'init':'epsg:4326'})
my_bird_gpd['geometry'] = my_bird_gpd['geometry'].to_crs(epsg=2229)

my_bird_gpd.plot(ax=my_ax, color='yellow')

plt.show()
