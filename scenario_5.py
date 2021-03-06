#!/usr/bin/env python

import rospy
import random
import math
from random import *

from geometry_msgs.msg import Twist

# sound module
from sound_publisher.msg import Tones
from sound_publisher.msg import TonesArray
from sound_publisher.msg import MusicalTones
from sound_publisher.msg import MusicalTonesArray
from sound_publisher.msg import SongTitle
from kobuki_msgs.msg import Sound

from turtlebot_scenario.msg import OrientationRequest
from kobuki_msgs.msg import BumperEvent

#face recognition
from facedetector.msg import Detection


# Global Variables
pub_motor = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=0)
pub_melody = rospy.Publisher('/mobile_base_commands/sound', Sound, queue_size = 0)
pub_Tones = rospy.Publisher('/sound/tones', TonesArray, queue_size = 1)
pub_MTones = rospy.Publisher('/sound/musical_note', MusicalTonesArray, queue_size =0)
pub_song = rospy.Publisher('sound/play_song', SongTitle, queue_size = 0)
pub_servo = rospy.Publisher('camera/orientation/request', OrientationRequest, queue_size = 0)

melody = Sound()
command = Twist()
song = SongTitle()
bumper = BumperEvent()
flag_detection = False

# easyly send command to the motor
def send_command_motor(linear = 0., angular = 0.):
	global pub_motor, command

	command.linear.x = linear
	command.linear.y = 0
	command.linear.z = 0
	command.angular.x = 0
	command.angular.y = 0
	command.angular.z = angular
	pub_motor.publish(command)
	rospy.sleep(0.1)

# randomly choose a sign
def sign():
	return choice([-1, 1])

# reaction to bumper hit

def callback_bumper(data):
	global bumper
	global pub_MTones	

	bumper = data
	#if bumper.bumper == bumper.LEFT:
		#pub_MTones.publish([MusicalTones('do', 8, 500)])
	#elif bumper.bumper == bumper.RIGHT:
		#pub_MTones.publish([MusicalTones('si', 8, 500)])
	#rospy.sleep(0.5)	


#reaction to a face recognition
def callback_face(face):
	global pub_Tones, flag_detection

	flag_detection = True
	pub_Tones.publish([Tones(2000, 500)])
	rospy.sleep(0.5)

def scenario():
	global melody, pub_melody
	global pub_Tones, pub_song, song
	global pub_servo
	global bumper

	if bumper.bumper == bumper.LEFT:
		send_command_motor(angular = -2.)
		rospy.sleep(0.8)
		bumper.bumper = 3
	elif bumper.bumper == bumper.CENTER:
		# Recule + levage camera
		flag_detection = False
		song.song = song.Star_Wars
		pub_song.publish(song)
		pub_servo.publish(True)
		send_command_motor(linear = -0.2)
		rospy.sleep(5)

		# People still standing
		while(flag_detection == True):
			flag_detection = False
			rospy.sleep(2.5)

		# robot going away
		pub_servo.publish(False)
		send_command_motor(linear = -0.2, angular = sign() *  2)
		rospy.sleep(1)
		bumper.bumper = 3
		
	elif bumper.bumper == bumper.RIGHT:
		send_command_motor(angular = 2.)
		rospy.sleep(0.8)
		bumper.bumper = 3
		
	else:
		send_command_motor(linear = 0.2)

	

def main():
	global bumper
	global pub_song, song

	rospy.sleep(2)
	
	# topic subscribed
	rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback_bumper)
	rospy.Subscriber('/facedetector/faces', Detection, callback_face)
	
	rospy.sleep(1)
	song.song = song.Indiana_Jones
	pub_song.publish(song)
	bumper.bumper = 3

	# moving loop
	while not rospy.is_shutdown():
		#randomm direction changing
		duree = 3 + random()*5
		time_end = rospy.get_time() + duree
		
		while(rospy.get_time() < time_end):
			scenario()
		if bumper > 2:
			print('aleatoire')
			bumper.bumper = choice([bumper.LEFT, bumper.RIGHT, 3])
	rospy.spin() 				

if __name__ == '__main__':
	rospy.init_node('scenario', anonymous=True)
	main()
