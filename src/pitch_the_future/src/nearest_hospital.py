#!/usr/bin/env python
# Importing required libraries
# from tokenize import Stringsss
from googleplaces import GooglePlaces, types, lang
import requests
import json
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String

def nearest_hospital(data):
	API_KEY = 'AIzaSyDzE2VUFnmOcgKehH165c4MBqGhOkyLRFI'

	# Initialising the GooglePlaces constructor
	google_places = GooglePlaces(API_KEY)

	# call the function nearby search with
	# the parameters as longitude, latitude,
	# radius and type of place which needs to be searched of
	# type can be HOSPITAL, CAFE, BAR, CASINO, etc
	query_result = google_places.nearby_search(
			# lat_lng ={'lat': 46.1667, 'lng': -1.15},
			lat_lng ={'lat': 28.4089, 'lng': 77.3178},
			radius = 5000,
			# types =[types.TYPE_HOSPITAL] or
			# [types.TYPE_CAFE] or [type.TYPE_BAR]
			# or [type.TYPE_CASINO])
			types =[types.TYPE_HOSPITAL])

	# If any attributions related
	# with search results print them
	if query_result.has_attributions:
		print (query_result.html_attributions)


	# Iterate over the search results
	for place in query_result.places:
		# print(type(place))
		# place.get_details()
		print (place.name)
		print("Latitude", place.geo_location['lat'])
		print("Longitude", place.geo_location['lng'])
		print()
		
	pub.publish(query_result.places[0].name)

pub = rospy.Publisher('nearest_hospitals', String, queue_size=10)
rospy.init_node('nearest_hospital', anonymous=True)

rospy.Subscriber("state", String, nearest_hospital)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()
# This is the way to make api requests
# using python requests library

# send_url = 'http://freegeoip.net/json'
# r = requests.get(send_url)

# j = json.loads(r.text)
# print(j)
# lat = j['latitude']
# lon = j['longitude']

# Generate an API key by going to this location
# https://cloud.google.com /maps-platform/places/?apis =
# places in the google developers

# Use your own API key for making api request calls
