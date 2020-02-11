#!/usr/bin/env python

from turtlebot_control import walk_forward,turn_clockwise
import rospy

if __name__ == '__main__':
    try:
        turn_clockwise(180)
    except rospy.ROSInterruptException:
        pass
