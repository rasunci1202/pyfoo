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
print(my_lacounty_gdf.crs)
print(my_lacounty_gdf)
#my_lacounty_gdf.plot(color='orange', edgecolor='black')
#matplotlib.pyplot.show()
my_lacounty_gdf = my_lacounty_gdf.to_crs(epsg=4326)
print(my_lacounty_gdf)
print(my_lacounty_gdf.total_bounds)
my_fig = matplotlib.pyplot.figure(figsize=(16, 10))
my_ax = matplotlib.pyplot.subplot(projection=cartopy.crs.Mercator(), figure=my_fig)
my_ax = geoplot.polyplot(my_lacounty_gdf, ax=my_ax, extent=(-118.8, 33.9, -118.0, 34.4))
matplotlib.pyplot.show()

#my_fig = matplotlib.pyplot.figure(figsize=(16, 10), tight_layout=True)
#my_fig.add_axes([118.537902, 33.488056, 117.725165, 34.789895])
#my_ax = my_fig.add_subplot()
#geoplot.polyplot(my_lacounty_gdf, projection=geoplot.crs.WebMercator())
#my_ax.set_xlim(6350000, 6650000)
#my_ax.set_ylim(1550000, 1900000)
#my_ax = my_lacounty_gdf.plot(ax=my_ax, color='orange', edgecolor='black')
#my_ax.set_xlim(-118.537902, -117.725165)
#my_ax.set_ylim(33.488056, 34.789895)

"""
my_p1 = Proj(init='epsg:2229')
my_p2 = Proj(proj='latlong', datum='WGS84')
my_lon, my_lat, my_z = transform(my_p1, my_p2, 6462560.206320852, 1779895.10190393, 0.0)
print(my_lon, my_lat, my_z)
"""
"""
my_lacounty_gdf = my_lacounty_gdf.to_crs(epsg=3857)
print(my_lacounty_gdf.crs)
print(my_lacounty_gdf)
#geoplot.polyplot(my_lacounty_gdf, projection=geoplot.crs.WebMercator(), figsize=(16, 10), ax=my_ax, extent=(-118.537902, 33.488056, -117.725165, 34.789895))
my_lacounty_gdf.plot(color='white', edgecolor='black')
matplotlib.pyplot.show()
"""
pass

"""
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
print(my_lime_df)
my_lime_geom = [Point(float(lon), float(lat)) for lon, lat in zip(my_lime_df['lon'], my_lime_df['lat'])]
print(my_lime_geom)
my_lime_geom_df = pandas.DataFrame(my_lime_geom, columns=['geometry'])
my_lime_gis_df = my_lime_df.join(my_lime_geom_df)
my_lime_gpd = geopandas.GeoDataFrame(my_lime_gis_df, crs={'init':'epsg:4326'})
my_lime_gpd['geometry'] = my_lime_gpd['geometry'].to_crs(epsg=2229)

my_lime_gpd.plot(ax=my_ax, color='blue')
#geoplot.kdeplot(my_lime_gpd, ax='my_ax')

matplotlib.pyplot.show()
"""
