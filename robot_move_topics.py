#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def move():
    speed_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    print ("1")
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 1hz
    i = 0
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 1.0
        twist.linear.y = 0.5
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.4
        rospy.loginfo(twist)
        speed_pub.publish(twist)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
