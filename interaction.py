import rospy
from geometry_msgs.msg import Twist
from cob_perception_msgs.msg import DetectionArray
from cob_perception_msgs.msg import ColorDepthImageArray

def image(data):
	print (data)


def main():
	
	print ("lancement interaction")
	rospy.init_node('interaction')
	rospy.sleep(0.5)
	rospy.Subscriber("/cob_people_detection/face_recognizer/face_recognitions", ColorDepthImageArray, image)
#	pub = rospy.Publisher("/mobile_base/commands/velocity", Twist)
#	cmd = Twist()
	
	while not rospy.is_shutdown():
		
#		pub.publish(cmd)

	print("fin interaction")
	rospy.spin()

if __name__ == "__main__":
	main()
