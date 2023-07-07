#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def odom_callback(msg):
    position = msg.pose.pose.position
    orientation = msg.pose.pose.orientation

    rospy.loginfo("Position: x=%f, y=%f, z=%f", position.x, position.y, position.z)
    rospy.loginfo("Orientation: x=%f, y=%f, z=%f, w=%f", orientation.x, orientation.y, orientation.z, orientation.w)

def odom_subscriber():
    rospy.init_node('odom_subscriber')
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.spin()

if __name__ == '__main__':
    odom_subscriber()
