#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pi

def walk_forward(dist):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = 50 # 50hz
    r = rospy.Rate(rate) 
    vel_msg = Twist()
    vel_msg.linear.x = 0.2
    for time in range(int(dist * rate * 5)):
        pub.publish(vel_msg)
        r.sleep()
    vel_msg.linear.x=0
    pub.publish(vel_msg)
    r.sleep()


def turn_clockwise(angle):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = 500 # 1hz
    angular_speed = -1.0
    goal_angle = pi * angle / 180
    angular_duration = goal_angle / angular_speed
    r = rospy.Rate(rate) 
    vel_msg = Twist()
    vel_msg.angular.z = angular_speed
    for time in range(int(goal_angle*rate)):
        pub.publish(vel_msg)
        r.sleep()
    vel_msg.angular.z=0
    pub.publish(vel_msg)
    r.sleep()
