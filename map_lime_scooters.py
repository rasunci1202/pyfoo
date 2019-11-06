import numpy
import matplotlib.pyplot as plt
import requests
import json
import pandas
import geopandas as gpd
import pyproj
import fiona
from shapely.geometry import Point, Polygon

my_lacounty_shapefile = 'c:/Users/rasunci/gitstuff/DPW_CITY_BOUNDARIES/DPW_CITY_BOUNDARIES.shp'
my_lacounty_gdf = gpd.read_file(my_lacounty_shapefile)

my_fig = plt.figure(figsize=(16, 10), tight_layout=True)
my_ax = my_fig.add_subplot()
my_ax.set_xlim(6350000, 6650000)
my_ax.set_ylim(1550000, 1900000)
my_lacounty_gdf.plot(ax=my_ax, color='orange', edgecolor='black')

my_url = 'https://lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status.json'
my_file = 'c:/Users/rasunci/gitstuff/lime/free_bike_status.json'
my_lime_data = ''
my_lime_locs = []

if (False):
    my_r = requests.get(my_url)
    if my_r.status_code == 200:
        my_lime_data = my_r.json()
    else:
        print('error handler here')
else:
    with open(my_file) as my_fh:
        my_json = my_fh.read()
    my_lime_data = json.loads(my_json)

my_lime_bikes = my_lime_data['data']['bikes']
#for i in range(150):
my_lime_count = len(my_lime_data['data']['bikes'])

for i in range(my_lime_count):
    my_bike = my_lime_bikes[i]['bike_id']
    my_lon = my_lime_bikes[i]['lon']
    my_lat = my_lime_bikes[i]['lat']
    #print(my_bike, end=' ')
    #print(my_lon, end=' ')
    #print(my_lat)
    my_lime_locs.append([my_bike, my_lon, my_lat])
"""
my_debug_file = 'c:/Users/rasunci/gitstuff/lime/errors'
my_debug_fh = ''
try:
    my_debug_fh = open(my_debug_file, 'w')
except:
    print('Cannot open ' + my_debug_file)
    quit()
"""
my_lime_df = pandas.DataFrame(my_lime_locs, columns=['bike_id', 'lon', 'lat'])
print(my_lime_df)
my_lime_geom = [Point(float(lon), float(lat)) for lon, lat in zip(my_lime_df['lon'], my_lime_df['lat'])]
print(my_lime_geom)
my_lime_geom_df = pandas.DataFrame(my_lime_geom, columns=['geometry'])
my_lime_gis_df = my_lime_df.join(my_lime_geom_df)
my_lime_gpd = gpd.GeoDataFrame(my_lime_gis_df, crs={'init':'epsg:4326'})
my_lime_gpd['geometry'] = my_lime_gpd['geometry'].to_crs(epsg=2229)

my_lime_gpd.plot(ax=my_ax, color='blue')

plt.show()

