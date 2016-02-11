import rospy
#import random
#from std_msgs.msg import Int16
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

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
	global bumper_ancien
	global cpt
	print("Lancement navigation aleatoire")
	rospy.init_node('navigation_aleatoire')
	rospy.sleep(0.5)
	rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, bumper)
	pub = rospy.Publisher("/mobile_base/commands/velocity", Twist)
	cmd = Twist()




	while not rospy.is_shutdown():


		if bumper==0:
			cmd.linear.x = 0
			cmd.angular.z = -2
			pub.publish(cmd)
			rospy.sleep(1.5)
			bumper=3
		elif bumper==1:
			cmd.linear.x = -0.5
			cmd.angular.z = 4
			pub.publish(cmd)
			rospy.sleep(3)
			bumper=3
		elif bumper==2:
			cmd.linear.x = 0
			cmd.angular.z = 2
			pub.publish(cmd)
			rospy.sleep(1.5)
			bumper=3
		else:
			cmd.linear.x = 0.5
			cmd.angular.z = 0
			pub.publish(cmd)
				#print(cmd)

	print("fin navigation autonome")
	rospy.spin() #boucle infinie tant qu'on quitte pas proprement


if __name__ == "__main__":
	main()
