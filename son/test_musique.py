

import kobuki_serial
import time

robot = kobuki_serial.Kobuki('/dev/kobuki')
a = 0.00000275

def note(f, t):
	global robot
	global a
	for i in range (0, t/200):
		robot.send([kobuki_serial.BuildRequestData.sound(int(1./(f*a)), 254)])
		time.sleep(0.1)
	time.sleep(0.25)

def main():
	global robot
	note(523, 250)
	note(523, 250)
	note(523, 250)
	note(587, 250)
	note(659, 500)
	note(587, 750)
	note(523, 500)
	note(659, 250)
	note(587, 250)
	note(587, 250)
	note(523, 750)

	

if __name__ == "__main__":
        main()


