import rospy
import random
import math

#from std_msgs.msg import Int16
from kobuki_msgs.msg import DigitalOutput

def main():
	global bumper
	print("Lancement test servo")
	rospy.init_node('test_servo')
	rospy.sleep(0.5)
	pub = rospy.Publisher("/mobile_base/commands/digital_output", DigitalOutput)
	cmd=DigitalOutput()
	cmd.values= [True, True, True, True]
	cmd.mask=[True, False, False, False]
	while not rospy.is_shutdown():
		print(cmd)
		pub.publish(cmd)
		cmd.values=[False, False, False, False]
		rospy.sleep(5)
		print(cmd)
		pub.publish(cmd)
		rospy.sleep(5)
		cmd.values= [True, True, True, True]
	print("je suis desole, je n'ai pas de servo")
	rospy.spin() #boucle infinie tant qu'on quitte pas proprement


if __name__ == "__main__":
	main()
