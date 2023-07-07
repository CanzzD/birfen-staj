#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(msg):
    linear_x = msg.linear.x
    angular_z = msg.angular.z

    rospy.loginfo("Received cmd_vel: linear_x=%.2f, angular_z=%.2f", linear_x, angular_z)

def cmd_vel_listener():
    rospy.init_node('cmd_vel_listener')
    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)
    rospy.spin()

if __name__ == '__main__':
    cmd_vel_listener()
