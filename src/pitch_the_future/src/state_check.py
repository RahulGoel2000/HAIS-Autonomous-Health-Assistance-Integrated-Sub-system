#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import String

def callback(data):
    if(data.data==1):
        pub.publish("critical")
    
def listener():
    global pub
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    pub = rospy.Publisher('state', String, queue_size=10)
    rospy.init_node('state_check', anonymous=True)

    rospy.Subscriber("ml_model_op", Int16, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()