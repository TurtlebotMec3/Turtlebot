#code by Julieng =!=

import rospy
import random
import math

#from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
from sound_play.msg import SoundRequest
from kobuki_msgs.msg import Sound
from kobuki_msgs.msg import DigitalOutput
from cob_perception_msgs.msg import ColorDepthImageArray
from cob_perception_msgs.msg import DetectionArray
from sensor_msgs.msg import Image


bumper = 3
NbGens = 0
Nbmax = 0

def bumper(data):
	global bumper

	#print(data.bumper)

	#	1
	#0 		2

	#print(data.state)

	# 0 relache
	# 1 appuye

	bumper = data.bumper

def image(data):
	global NbGens
	global Nbmax
	NbGens=len(data.detections)
	if NbGens>Nbmax:
		Nbmax=NbGens




def main():
	global bumper
	global Nbmax
	global Nbgens
	print("Lancement navigation aleatoire")
	rospy.init_node('navigation_aleatoire')
	rospy.sleep(0.5)
	rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, bumper)
	rospy.Subscriber("/cob_people_detection/face_recognizer/face_recognitions", DetectionArray, image)
	pub = rospy.Publisher("/mobile_base/commands/velocity", Twist)
	pub2 = rospy.Publisher("/robotsound", SoundRequest)
	pub3 = rospy.Publisher("/mobile_base/commands/sound", Sound)
	pub4 = rospy.Publisher("/mobile_base/commands/digital_output", DigitalOutput)
	cmd = Twist()
	sound = SoundRequest()
	sonnerie = Sound()
	sonnerie2 = Sound()
	sound.arg = "/opt/ros/indigo/share/sound_play/sounds/R2D2a.wav"
	sound.sound = -2
	sound.command = 1
	sonnerie.value= 6
	sonnerie2.value= 5
	digOut=DigitalOutput()
	digOut.values= [False, False, False, False]
	digOut.mask=[True, False, False, False]
	pub4.publish(digOut)
	rospy.sleep(0.5)
	flag1=0
	flag2=0
	print(digOut)

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
				cmd.angular.z = 0
				digOut.values[0]=True
				pub.publish(cmd)
				pub2.publish(sound)
				pub4.publish(digOut)
				rospy.sleep(5)
				while (NbGens>0):
					rospy.sleep(2.5)
					flag1=1
					if (Nbmax>1):
						if (Nbgens>1):
							pub3.publish(sonnerie2)
							rospy.sleep(0.5)
				digOut.values[0]=False
				if flag1==1:
					rospy.sleep(2)
					pub3.publish(sonnerie)
					rospy.sleep(0.5)
					flag1=0
					Nbmax=0
				pub4.publish(digOut)
				rospy.sleep(0.5)
				cmd.linear.x = -0.2
				cmd.angular.z = 2
				pub.publish(cmd)
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
			if bumper == 1:
				bumper=3
	print("fin navigation autonome")
	digOut.values[0]=False
	pub4.publish(digOut)
	rospy.sleep(0.5)
	rospy.spin()


if __name__ == "__main__":
	main()


