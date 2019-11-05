import numpy
import matplotlib.pyplot
import requests
import json
import pandas
import geopandas
import pyproj
import fiona
from shapely.geometry import Point, Polygon
import geoplot
import geoplot.crs
import folium
from folium.plugins import HeatMap
from pyproj import Proj, transform
import cartopy

pass

my_lacounty_shapefile = 'c:/Users/rasunci/gitstuff/DPW_CITY_BOUNDARIES/DPW_CITY_BOUNDARIES.shp'
my_lacounty_gdf = geopandas.read_file(my_lacounty_shapefile)
#print(my_lacounty_gdf.crs)
#print(my_lacounty_gdf)
#my_lacounty_gdf.plot(color='orange', edgecolor='black')
#matplotlib.pyplot.show()
my_lacounty_gdf = my_lacounty_gdf.to_crs(epsg=4326)
print(my_lacounty_gdf)
print(my_lacounty_gdf.total_bounds)
my_fig = matplotlib.pyplot.figure(figsize=(16, 10))
my_ax = matplotlib.pyplot.subplot(projection=cartopy.crs.Mercator(), figure=my_fig)
my_ax = geoplot.polyplot(my_lacounty_gdf, ax=my_ax, extent=(-118.8, 33.9, -118.0, 34.4))
#matplotlib.pyplot.show()


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
my_lime_count = len(my_lime_data['data']['bikes'])
for i in range(my_lime_count):
    my_bike = my_lime_bikes[i]['bike_id']
    my_lon = my_lime_bikes[i]['lon']
    my_lat = my_lime_bikes[i]['lat']
    my_lime_locs.append([my_bike, my_lon, my_lat])

my_lime_df = pandas.DataFrame(my_lime_locs, columns=['bike_id', 'lon', 'lat'])
my_lime_geom = [Point(float(lon), float(lat)) for lon, lat in zip(my_lime_df['lon'], my_lime_df['lat'])]
my_lime_geom_df = pandas.DataFrame(my_lime_geom, columns=['geometry'])
my_lime_gis_df = my_lime_df.join(my_lime_geom_df)
my_lime_gdf = geopandas.GeoDataFrame(my_lime_gis_df, crs={'init':'epsg:4326'})
print(my_lime_gdf)

#my_ax = geoplot.pointplot(my_lime_gdf, ax=my_ax)
my_ax = geoplot.kdeplot(my_lime_gdf, ax=my_ax, n_levels=20, shade=False, shade_lowest=False, cmap='Greens')

matplotlib.pyplot.show()

