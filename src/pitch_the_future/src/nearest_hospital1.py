#!/usr/bin/env python

# Importing required libraries
# from tokenize import Stringsss

from googleplaces import GooglePlaces, types, lang
import requests
import json
import rospy
from std_msgs.msg import Int16
from sensor_msgs.msg import Imu, MagneticField, NavSatFix
from std_msgs.msg import String

class Hospital(object):

    def gps_cb(self, coord):
        self.lat = coord.latitude
        self.long = coord.longitude

    def state_cb(self, data):
        if data.data=="critical":
            self.nearest_hospital()

    def nearest_hospital(self, data):
        API_KEY = 'AIzaSyDzE2VUFnmOcgKehH165c4MBqGhOkyLRFI'

		# Initialising the GooglePlaces constructor
        google_places = GooglePlaces(API_KEY)

		# call the function nearby search with
		# the parameters as longitude, latitude,
		# radius and type of place which needs to be searched of
		# type can be HOSPITAL, CAFE, BAR, CASINO, etc
        query_result = google_places.nearby_search(
				# lat_lng ={'lat': 46.1667, 'lng': -1.15},
				lat_lng ={'lat': self.lat, 'lng': self.long},
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

        pub = rospy.Publisher('nearest_hospitals', String, queue_size=10)
        pub.publish(query_result.places[0].name)

    def __init__(self):
        rospy.Subscriber("gps/fix", NavSatFix, self.gps_cb)
        rospy.Subscriber("state", String, self.state_cb)
        rospy.spin()
			   		

if __name__== "__main__":
    rospy.init_node("nearest_hospital1",anonymous=False)
    ld = Hospital()