import numpy
import matplotlib.pyplot as plt
import requests
import json
import pandas
import geopandas as gpd
import pyproj
import fiona
from shapely.geometry import Point, Polygon

#my_file = 'c:/Users/bisuser/Downloads/DAMSELFISH/DAMSELFISH_distributions.shp'
#my_file = 'c:/Users/bisuser/Downloads/LA_County_City_Boundaries.shp' # Fiona/GDAL error
#my_file = 'c:/Users/bisuser/Downloads/City_of_Los_Angeles_Bikeways.shp' # Fiona/GDAL error
#my_file = 'c:/Users/bisuser/Downloads/DPW_COUNTY_BOUNDARY/DPW_COUNTY_BOUNDARY.shp'
my_file = 'c:/Users/bisuser/Downloads/DPW_CITY_BOUNDARIES/DPW_CITY_BOUNDARIES.shp'
my_data = gpd.read_file(my_file)

"""
my_data.plot()
plt.show()
"""

print(type(my_data))
print(my_data.head())
print('CRS=', my_data.crs)
print(my_data.geometry.name)

my_fig = plt.figure(figsize=(16, 10), tight_layout=True)
my_ax = my_fig.add_subplot()

my_ax.set_xlim(6350000, 6650000)
my_ax.set_ylim(1550000, 1900000)
my_data.plot(ax=my_ax, color='orange', edgecolor='black')


#plt.show()

my_cities = [
    ('Alhambra', 'USA', 34.097220, -118.126567),
    ('Catalina', 'USA', 33.395225, -118.416478),
    ('Long Beach', 'USA', 33.758529, -118.190804),
    ('Santa Monica', 'USA', 34.021868, -118.471286)
    ]
print(my_cities)
my_cities_df = pandas.DataFrame(my_cities)
print(my_cities_df)

my_xy = [[city[2],city[3]] for city in list(my_cities)]
my_xy_ndarray = numpy.asarray(my_xy)
print("my_xy_ndarray shape=", my_xy_ndarray.shape)
print(my_xy_ndarray)
print("my_xy_ndarray[:,0] shape=", my_xy_ndarray[:,0].shape)
print(my_xy_ndarray[:,0])
print("my_xy_ndarray[:1] shape=", my_xy_ndarray[:,1].shape)
print(my_xy_ndarray[:,1])

#print(my_xy_ndarray[:,0], my_xy_ndarray[:,1])

my_cities_geometry = [Point(lon, lat) for lat, lon in zip(my_xy_ndarray[:,0], my_xy_ndarray[:,1])]
print(my_cities_geometry[0])

my_cities_gpd = gpd.GeoDataFrame(my_cities_df, crs={'init':'epsg:4326'}, geometry=my_cities_geometry)
print(my_cities_gpd)

my_cities_gpd['geometry'] = my_cities_gpd['geometry'].to_crs(epsg=2229)
print('New CRS=', my_cities_gpd.crs)
print(my_cities_gpd)

my_cities_gpd.plot(ax=my_ax, color='green')

plt.show()


