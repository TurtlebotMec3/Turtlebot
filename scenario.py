import rospy
import random
import math

#from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from sound_play.msg import SoundRequest
from kobuki_msgs.msg import Sound


bumper = 3
direction = 3

def bumper(data):
	global bumper
	global direction
	#print(data.bumper)

	#	1
	#0 		2

	#print(data.state)

	# 0 relache
	# 1 appuye

	bumper = data.bumper
	#if data.state == 1:
	#	direction = bumper
	#else:
	#	direction=3



def main():
	global bumper
	global direction
	print("Initialisation")
	rospy.init_node('scenario')
	rospy.sleep(0.5)
	rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, bumper)
	pub1 = rospy.Publisher("/mobile_base/commands/velocity", Twist)
	pub2 = rospy.Publisher("/robotsound", SoundRequest)
	pub3 = rospy.Publisher("/mobile_base/commands/sound", Sound)
	cmd = Twist()
	sound = SoundRequest()
	bip = Sound()
	sound.arg = "/opt/ros/indigo/share/sound_play/sounds/R2D2a.wav"
	sound.sound = -2
	sound.command = 1
	bip.value=4
	while not rospy.is_shutdown():

		duree= 1+random.random()*5
		tempsActuel = rospy.get_time()
		stop = rospy.get_time() + duree
		while (rospy.get_time() < stop):
			if bumper==0:
				cmd.linear.x = 0
				cmd.angular.z = 0
				pub2.publish(sound)
				rospy.sleep(0.5)
				pub1.publish(cmd)
				rospy.sleep(5)
				cmd.linear.x = -0.2
				cmd.angular.z = -2
				cmd.angular.z = -2
				pub1.publish(cmd)
				rospy.sleep(0.5)
				bumper == 3
			elif bumper==1:
				cmd.linear.x = -0.2
				pub1.publish(cmd)
				pub3.publish(bip)
				rospy.sleep(0.5)
				bumper == 3
			elif bumper==2:
				cmd.linear.x = 0
				cmd.angular.z = 2
				pub1.publish(cmd)
				rospy.sleep(0.5)
				bumper== 3
			else:
				cmd.linear.x = 0.2
				cmd.angular.z = 0
				pub1.publish(cmd)
		if bumper>2:
			bumper = math.floor(random.random()*10)

	print("The End")
	rospy.spin()


if __name__ == "__main__":
	main()
