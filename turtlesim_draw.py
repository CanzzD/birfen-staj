#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pi

def draw_triangle():
    rospy.init_node('turtle_draw')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)

    move_cmd = Twist()

    for _ in range(4):
        move_cmd.linear.x = 2.0
        move_cmd.angular.z = 0.0 
        pub.publish(move_cmd)
        rospy.sleep(2.0)
        move_cmd.linear.x = 0.0
        pub.publish(move_cmd)
        rospy.sleep(1.0)
        move_cmd.angular.z = 2.0944 #2*pi/3 120 derece
        pub.publish(move_cmd)
        rospy.sleep(1.0)

def draw_square():
    rospy.init_node('turtle_draw')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)

    move_cmd = Twist()

    for _ in range(5):
        move_cmd.linear.x = 2.0
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)
        rospy.sleep(2.0)
        move_cmd.linear.x = 0.0
        pub.publish(move_cmd)
        rospy.sleep(1.0)
        move_cmd.angular.z = 1.57 #pi/2 90 derece
        pub.publish(move_cmd)
        rospy.sleep(1.0) 

def draw_circle():
    rospy.init_node('turtle_draw')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    move_cmd = Twist()

    move_cmd.linear.x = 2.0
    move_cmd.angular.z = pi / 2 # 10 derece dön

    for _ in range(50):
        pub.publish(move_cmd)
        rate.sleep()

    stop_cmd = Twist()
    pub.publish(stop_cmd)

if __name__ == '__main__':
    print("Turtlesim Robotu İçin Çizim Seçimi")
    print("1 - Üçgen")
    print("2 - Kare")
    print("3 - Yuvarlak")

    choice = int(input("Bir seçenek girin: "))

    if choice == 1:
        draw_triangle()
    elif choice == 2:
        draw_square()
    elif choice == 3:
        draw_circle()
    else:
        print("Geçersiz bir seçenek girdiniz.")