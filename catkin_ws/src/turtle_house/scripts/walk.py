#!/usr/bin/env python

from turtlebot_control import walk_forward,turn_clockwise,turn_counterclockwise,sleep
import rospy

if __name__ == '__main__':
    try:
        sleep(3)
        turn_counterclockwise(85)
        walk_forward(5.2)
        turn_clockwise(90)
        walk_forward(6)
        turn_clockwise(10)
        sleep(3)
        #initial
        walk_forward(1)
        turn_clockwise(120)
        walk_forward(1.5)
        turn_counterclockwise(120)
        walk_forward(1)
    except rospy.ROSInterruptException:
        pass
