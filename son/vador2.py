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
        time.sleep(0.2)

def main():
        note(440, 500)
	note(440, 500)
	note(440, 500)
	note(349, 376)
	note(523, 200)
	note(440, 500)
	note(349, 376)
	note(523, 200)
	note(440, 1000)

	note(659, 500)
	note(659, 500)
	note(659, 500)
	note(698.5, 376)
	note(523, 200)
	note(415, 500)
	note(349, 376)
	note(523, 200)
	note(440, 1000)

if __name__ == "__main__":
        main()

