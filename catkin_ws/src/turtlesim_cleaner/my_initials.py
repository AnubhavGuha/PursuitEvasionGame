#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
    # Starts a new node
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

    #Receiveing the user's input
	print("Let's move your robot")
	speed = input("Input your speed:")
	radius = input("Type your radius:")
	speed = input("Input your speed (degrees/sec):")
	angle = input("Type your distance (degrees):")
	clockwise = input("Clockwise?: ") #True or false
	#isForward = input("Foward?: ")#True or False

	angular_speed = speed*2*PI/360
	relative_angle = angle*2*PI/360
    #Checking if the movement is forward or backwards
	if(isForward):
		vel_msg.linear.x = abs(speed)
	else:
		vel_msg.linear.x = -abs(speed)

	#Since we are moving just in x-axis
	vel_msg.linear.x = speed
	vel_msg.linear.y = speed
	vel_msg.linear.z = speed
	vel_msg.angular.x = speed
	vel_msg.angular.y = speed
	#vel_msg.angular.z = speed/radius
	"""
	#Move Robot in circle
	if clockwise:
		vel_msg.angular.z = -abs(angular_speed)
	else:
		vel_msg.angular.z = abs(angular_speed)
	# Setting the current time for distance calculus
	t0 = rospy.Time.now().to_sec()
	current_angle = 0

	while(current_angle < relative_angle):
		velocity_publisher.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_angle = angular_speed*(t1-t0)
	"""

	#Forcing our robot to stop
	vel_msg.angular.z = 0
	velocity_publisher.publish(vel_msg)
	rospy.spin()

def move_circle_server():
	rospy.init_node('my_initials')
	move()
	rospy.spin()



if __name__ == '__main__':
    move_circle_server()
