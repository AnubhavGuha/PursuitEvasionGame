#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	speed = 3
	distance = 9
	isForward = 0
	if(isForward):
		vel_msg.linear.x = abs(speed)
	else:
		vel_msg.linear.x = -abs(speed)
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 1.8
	c=0
	while c==0:
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		while(current_distance < distance):
			velocity_publisher.publish(vel_msg)
			t1=rospy.Time.now().to_sec()
			current_distance= speed*(t1-t0)
		vel_msg.linear.x = 0
		vel_msg.angular.z = 0
		#current_distance = 0;
		#vel_msg.angular.z = 0
		#t0 = rospy.Time.now().to_sec()
		"""
		while(current_distance < distance):
            #Publish the velocity
			velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
			t1=rospy.Time.now().to_sec()
			current_distance= speed*(t1-t0)
		"""
		#Force the robot to stop
		velocity_publisher.publish(vel_msg)
		c=1
	vel_msg.angular.z = -1.5
	velocity_publisher.publish(vel_msg)	
	#vel_msg.angular.z = 0
	vel_msg.linear.x = 1
	velocity_publisher.publish(vel_msg)
if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
