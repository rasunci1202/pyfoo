# Modules
import requests
import json
import pandas
import numpy
import matplotlib.pyplot as plt


# Globals
my_data = {}
# Constants
SWAPI_BASE_URL     = 'https://swapi.co/api'
SWAPI_URL_TYPES    = ['people'] # Also planets, starships, etc
SWAPI_URL_TYPE_ARG = '/?page='
SWAPI_PLOT_CHAR_ID = 'Character ID'
SWAPI_PLOT_MASS    = 'Mass'
SWAPI_PLOT_HEIGHT  = 'Height'
SWAPI_R_RESULTS    = 'results'
SWAPI_R_NAME       = 'name'
SWAPI_R_MASS       = 'mass'
SWAPI_R_HEIGHT     = 'height'


# Parse JSON and build data dictionary
def collect_swapi_data(my_json):
    global my_data
    
    my_item_count = len(my_json[SWAPI_R_RESULTS])
    for i in range(my_item_count):
        my_name = my_json[SWAPI_R_RESULTS][i][SWAPI_R_NAME]
        my_mass = my_json[SWAPI_R_RESULTS][i][SWAPI_R_MASS]
        my_height = my_json[SWAPI_R_RESULTS][i][SWAPI_R_HEIGHT]
        my_string = my_name + " " + my_mass + " " + my_height
        # For debugging. Show string
        print(my_string)
        
        # Grow the dictionary:
        # Try casting "mass" data to int
        try:
            my_mass_int = int(my_mass)
        except ValueError:
            my_mass_int = 0      
        # Try casting "height" data to int
        try:
            my_height_int = int(my_height)
        except ValueError:
            my_height_int = 0            
        my_ID = len(my_data.keys())
        my_data[my_name] = [my_ID, my_mass_int, my_height_int]

# Fetch consecutive SWAPI pages
def get_swapis(my_url):
    my_page = 1
    # Starting with page 1, fetch the page and grow the SWAPI dictionary.
    # Continue to increment page number and fetch until return code is an error
    while(True):
        my_next_url = my_url + SWAPI_URL_TYPE_ARG + str(my_page)
        my_r = requests.get(my_next_url)
        if my_r.status_code == 200: # HTTP OK
            my_json = my_r.json()
            collect_swapi_data(my_json)
            my_page = my_page + 1
        if my_r.status_code >= 400: # HTTP Client or Server Error
            # Error handler here
            break            
        

# Loop through list of SWAPI types
for my_swapi_type in SWAPI_URL_TYPES:
    my_url = SWAPI_BASE_URL + '/' + my_swapi_type
    get_swapis(my_url)

# For debugging. Convert data to series and test
my_series = pandas.Series(my_data)
print(my_series.head(3))
print(my_series.tail(3))

# For debugging. Convert data to ndarray and test
my_list = [v for k,v in my_series.items()]
my_numpy_list = numpy.array(my_list)
print(my_numpy_list)
print('dim=' + str(my_numpy_list.ndim) + ', ' +
      'shape=' + str(my_numpy_list.shape) + ', ' +
      'size=' + str(my_numpy_list.size) + ', ' +
      'dtype=' + str(my_numpy_list.dtype) + ', ' +
      'itemsize=' + str(my_numpy_list.itemsize) + ', ' +
      'nbytes=' + str(my_numpy_list.nbytes))

# Create 2d matrix from 1st and 2nd cols
my_matrix = my_numpy_list[0:, :2]
print(my_matrix)
plt.plot(*zip(*my_matrix))
#plt.xticks(my_matrix[0:,:1])
plt.xlabel(SWAPI_PLOT_CHAR_ID)
plt.ylabel(SWAPI_PLOT_MASS)
plt.show()

 # Create 2d matrix from 1st and 3rd cols
my_matrix = my_numpy_list[0:, ::2]
print(my_matrix)
plt.plot(*zip(*my_matrix))
#plt.xticks(my_matrix[0:,:1])
plt.xlabel(SWAPI_PLOT_CHAR_ID)
plt.ylabel(SWAPI_PLOT_HEIGHT)
plt.show()
