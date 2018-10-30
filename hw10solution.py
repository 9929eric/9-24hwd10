# Import the module (top of the file).
import requests


# Make sure to replace [YOUR_API_KEY_HERE] with your actual key, which
# will look like a bunch of letters and numbers! Alternatively, copy the sample
# API call from Dark Sky dashboard and just remove the coordinates.
API_BASE_URL = 'https://api.darksky.net/forecast/6b2b7fb590bf36377bce56a994b9f2ef/'

import geocoder
# Declare destinations list here.
destinations = ['Space Needle',
'Crater Lake',
'Golden Gate Bridge',
'Yosemite National Park',
'Las Vegas, Nevada',
'Grand Canyon National Park',
'Aspen, Colorado',
'Mount Rushmore',
'Yellowstone National Park',
'Sandpoint, Idaho',
'Banff National Park',
'Capilano Suspension Bridge']

for point in destinations:

#   Get the lat-long coordinates from `geocoder.arcgis`.
  g = geocoder.arcgis(point)
 #   Print out the place name and the coordinates.
# latlng is a tuple with a length of 2.
  print(point, 'is located at('+'{0:.4f}'.format(g.latlng[0]),'{0:.4f}'.format(g.latlng[1])+')')

# full_api_url = API_BASE_URL + latitude + "," + longitude

  full_api_url = (API_BASE_URL + str(g.latlng[0]) + "," + str(g.latlng[1]))
    # where latitude and longitude are the values contained in `point`
  result = requests.request('GET',full_api_url).json()

    # From the result, print out the summary and current temperature.
  print("At", point,"right now, it's", (result['currently']['summary']),'with a temperature of', '{0:.1f}'.format(result['currently']['temperature'])+'\u00b0'+' F')
  print(' ')
