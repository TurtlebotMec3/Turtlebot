#code by julieng =!=

import rospy
import random
import math
import cv2
import numpy as np

#from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent
#from sound_play.msg import SoundRequest
from kobuki_msgs.msg import Sound
from kobuki_msgs.msg import DigitalOutput
#from cob_perception_msgs.msg import ColorDepthImageArray
#from cob_perception_msgs.msg import DetectionArray
#from facedetector.msg import Detection 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


bumper = 3
NbGens = 0

class image_converter:
	
	def __init__(self):
		
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("camera/depth/image_rect",Image,self.callback)

	def callback(self,data):
		global bumper
		#data.height row
		#data.width columns	
		image_temp=self.bridge.imgmsg_to_cv2(data,"32FC1")
#		print(image_temp)
		dist_max_xtion=3.5
		dist_min_xtion=0.45
#		image_temp=np.clip(image_temp,0,dist_max_xtion)	
#		scaling_factor=255/dist_max_xtion
#		image_temp=image_temp*scaling_factor
#		print(image_temp)
		imageCV=np.array(image_temp,dtype=np.float32)
#		imageCV=convertTo(image_temp,CV_8U,0,3.5)
		cv2.normalize(imageCV,imageCV,0,1,cv2.NORM_MINMAX)
		print (imageCV[200][200][0])
		#imageCV[Dim1][Dim2][channel]
		#channel = 0
#		cv2.imshow("display",image_temp)
#		cv2.waitKey(3)

def bumper(data):
	global bumper

	#print(data.bumper)

	#	1
	#0 		2

	#print(data.state)

	# 0 relache
	# 1 appuye

	bumper = data.bumper

def face(data):
	global NbGens
	NbGens=len(data.image)



def main():
	global bumper

	print("Lancement navigation aleatoire")
	rospy.init_node('navigation_aleatoire')
	rospy.sleep(0.5)
	rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, bumper)
#	rospy.Subscriber("/facedetector/faces",Detection , face)
#	rospy.Subscriber("/camera/depth/image_rect",Image, image)
	pub = rospy.Publisher("/mobile_base/commands/velocity", Twist)
#	pub2 = rospy.Publisher("/robotsound", SoundRequest)
	pub3 = rospy.Publisher("/mobile_base/commands/sound", Sound)
	pub4 = rospy.Publisher("/mobile_base/commands/digital_output", DigitalOutput)
	
	ic=image_converter()

	cmd = Twist()
#	sound = SoundRequest()
	sonnerie = Sound()
#	sound.arg = "/opt/ros/indigo/share/sound_play/sounds/R2D2a.wav"
#	sound.sound = -2
#	sound.command = 1
	sonnerie.value= 6
	digOut=DigitalOutput()
	digOut.values= [False, False, False, False]
	digOut.mask=[True, False, False, False]
	flag=0


	while not rospy.is_shutdown():

		duree= 1+random.random()*5
		tempsActuel = rospy.get_time()
		stop = rospy.get_time() + duree
		while (rospy.get_time() < stop):
			if bumper==0:
				cmd.linear.x = 0
				cmd.angular.z = -2
#				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			elif bumper==1:
				cmd.linear.x = -0.2
				cmd.angular.z = 0
				digOut.values[0]=True
#				pub.publish(cmd)
#				pub2.publish(sound)
				pub4.publish(digOut)
				rospy.sleep(5)
				while (NbGens>0):
					rospy.sleep(2.5)
					flag=1
				digOut.values[0]=False
				if flag==1:
					pub3.publish(sonnerie)
					rospy.sleep(0.5)
					flag=0
				pub4.publish(digOut)
				rospy.sleep(0.5)
				cmd.linear.x = -0.2
				cmd.angular.z = 2
#				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			elif bumper==2:
				cmd.linear.x = 0
				cmd.angular.z = 2
#				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			else:
				cmd.linear.x = 0.2
				cmd.angular.z = 0
#				pub.publish(cmd)
		if bumper>2:
			bumper = math.floor(random.random()*10)
			if bumper == 1:
				bumper=3
	print("fin navigation autonome")
	rospy.spin() #boucle infinie tant qu'on quitte pas proprement


if __name__ == "__main__":
	main()


