import rospy
import random
import math

#from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from sound_play.msg import SoundRequest

bumper = 3

def bumper(data):
	global bumper

	#print(data.bumper)

	#	1
	#0 		2

	#print(data.state)

	# 0 relache
	# 1 appuye

	bumper = data.bumper


def main():
	global bumper
	print("Lancement navigation aleatoire")
	rospy.init_node('navigation_aleatoire')
	rospy.sleep(0.5)
	rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, bumper)
	pub = rospy.Publisher("/mobile_base/commands/velocity", Twist)
	pub2 = rospy.Publisher("/robotsound", SoundRequest)
	cmd = Twist()
	sound = SoundRequest()
	sound.arg = "/opt/ros/indigo/share/sound_play/sounds/R2D2a.wav"
	sound.sound = -2
	sound.command = 1

	while not rospy.is_shutdown():

		duree= 1+random.random()*5
		tempsActuel = rospy.get_time()
		stop = rospy.get_time() + duree
		while (rospy.get_time() < stop):
			if bumper==0:
				cmd.linear.x = 0
				cmd.angular.z = -2
				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			elif bumper==1:
				cmd.linear.x = -0.2
				cmd.angular.z = -2
				pub.publish(cmd)
				pub2.publish(sound)
				rospy.sleep(0.5)
				bumper=3
			elif bumper==2:
				cmd.linear.x = 0
				cmd.angular.z = 2
				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			else:
				cmd.linear.x = 0.2
				cmd.angular.z = 0
				pub.publish(cmd)
		if bumper>2:
			bumper = math.floor(random.random()*10)
		print(sound)

	print("fin navigation autonome")
	rospy.spin() #boucle infinie tant qu'on quitte pas proprement


if __name__ == "__main__":
	main()
