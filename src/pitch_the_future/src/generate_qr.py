#!/usr/bin/env python
import pyqrcode
import png
from pyqrcode import QRCode
import rospy
from std_msgs.msg import String
  
class QR(object):

    def __init__(self):
        
        rospy.Subscriber("/qr_link", String, self.cb)
        rospy.spin()

    def cb(self,link):
        # String which represents the QR code
        s = "https://www.teamaverera.com/"
        s= link.data
        # Generate QR code
        url = pyqrcode.create(s)
        
        # Create and save the svg file naming "myqr.svg"
        url.svg("myqr.svg", scale = 8)
        
        # Create and save the png file naming "myqr.png"
        url.png('myqr.png', scale = 6)


if __name__== "__main__":
    rospy.init_node("generate_qr",anonymous=False)
    ld = QR()