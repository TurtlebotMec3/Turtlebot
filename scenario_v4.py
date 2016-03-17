
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


bumper = ''
bumper1 = 3
NbGens = 0
flag = 0
class image_converter:
	
	def __init__(self):
		
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("camera/depth/image_rect",Image,self.callback)

	def callback(self,data):
		global bumper1
		#data.height row 480
		#data.width columns 640
		H=data.height
		W=data.width	
		image_temp=self.bridge.imgmsg_to_cv2(data,"16UC1")
		dist_max_xtion=3.5
#		dist_min_xtion=0.45
		imageCV=np.array(image_temp,dtype=np.float32)
		cv2.normalize(imageCV,imageCV,0,1,cv2.NORM_MINMAX)
#		print(data.height/2)
#		print(data.width/2)		
#		print (imageCV.shape)
		#print(imageCV[200][100][0],imageCV[200][200][0],imageCV[200][300][0])
		
		#imageCV[heigth][width][channel]
		#channel = 0	
#		print(H,W)
		#maskG=imageCV[H/3:][:W/4][0]
		#maskM=imageCV[H/3:][W/3:2*W/3][0]
		#maskD=imageCV[H/3:][W/4:][0]
#		imageCV == 'NaN' = 0
		
		# On decoupe l'image en 3 zones
		# On garde tout ce qui est a heuteur du robot
		# on coupe les bords noirs et on enleve le sol	
		# puis on decoupe une zone a gauche, une zone a droite et une zo		ne au centre
		# On fait ensuite un masque pour connaitre les points < 30 cm du 		robot
		maskG=imageCV[H/2-20:H-50,20:20+W/4,0]<0.1
                maskM=imageCV[H/2-20:H-50,W/3:2*W/3,0]<0.1
                maskD=imageCV[H/2-20:H-50,3*W/4-40:W-40,0]<0.1

		# On fait la moyenne des masques precedant pour connaitre le 
		# pourcentge de la zone < 30 cm
		valG=np.average(maskG)
		valM=np.average(maskM)
		valD=np.average(maskD)
		global flag

		if flag>100 and flag<120:
			cv2.imwrite("maskM.png",maskM*255)
			cv2.imwrite("maskG.png",maskG*255)
			cv2.imwrite("maskD.png",maskD*255)
			cv2.imwrite("image.png",imageCV[:,:,0]*255)
			print("~~~~~~~~~~~~")
			flag=130
		elif flag<120:
			flag=flag+1
		

		# Si 30 % de la zone est a moins de 30% du robot;
		# alors on considere qu'il y a un obstacle 
		# On retient la zone qui a le plus grand pourcentage
		if valG>0.25 and valG>valM and valG>valD :
			bumper1 = 0
		elif valM>0.25 and valM >valG and valM > valD:
			bumper1 = 1
		elif valD>0.25:
			bumper1 = 2
		else:
			bumper1 = 3
		print (bumper1)	
		print(valG,valM,valD)
#		mask=imageCV>0.5
#		print(np.average(mask))

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
			if bumper==0 or bumper1 ==0 :
				cmd.linear.x = 0
				cmd.angular.z = -2
				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			elif bumper==1 or bumper1==1:
				cmd.linear.x = -0.2
				cmd.angular.z = 0
				digOut.values[0]=True
				pub.publish(cmd)
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
				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			elif bumper==2 or bumper1==2:
				cmd.linear.x = 0
				cmd.angular.z = 2
				pub.publish(cmd)
				rospy.sleep(0.5)
				bumper=3
			else:
				cmd.linear.x = 0.2
				cmd.angular.z = 0
				pub.publish(cmd)
				rospy.sleep(0.5)
#		if bumper>2:
#			bumper = math.floor(random.random()*10)
#			if bumper == 1:
#				bumper=3
	print("fin navigation autonome")
	rospy.spin() #boucle infinie tant qu'on quitte pas proprement


if __name__ == "__main__":
	main()


