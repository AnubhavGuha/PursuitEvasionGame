#!/usr/bin/env python

from turtlebot_control import walk_forward,turn_clockwise,turn_counterclockwise
import rospy

if __name__ == '__main__':
    try:
        turn_counterclockwise(90)
        walk_forward(5.1)
        turn_counterclockwise(90)
        walk_forward(2)
        turn_clockwise(180)
        walk_forward(7)
        turn_clockwise(15)
        walk_forward(2)
        turn_counterclockwise(5)
        walk_forward(2)
        turn_clockwise(170)
        walk_forward(3.5)
        turn_clockwise(270)
        walk_forward(3)
        turn_clockwise(180)
        walk_forward(4)

        #initial
        turn_clockwise(90)
        walk_forward(1)
        turn_clockwise(120)
        walk_forward(2)
        turn_counterclockwise(120)
        walk_forward(1)
    except rospy.ROSInterruptException:
        pass
