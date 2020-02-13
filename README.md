# PursuitEvasionGame
Google Drive: https://drive.google.com/open?id=1PYka5h5mkiYNrWBjGywbiv76vJD6zBA2

2.11 2020 Update:
Update the turtle_house package.

Usage:

1. Copy turtle_house package to your catkin_ws/src.
2. Replace the home path of world file to your own.
3. under catkin_ws directory do: 
	catkin_make
	source devel/setup.bash
4. launch the world,
	roslaunch turtle_house turtle_house.launch
5. at a new terminal,
	rosrun image_view image_view image:=/camera/image_raw
6. at a new terminal,
	rosrun turtle_house walk.py

#IMPORTANT#

Due to the simulation environment, the turtlebot always slips and slides on the floor. So the code could not always work. If you find it doesn't visit each room or just crash the wall, please stop all the terminal program relaunch the environment.
