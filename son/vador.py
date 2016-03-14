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
        note(880, 500)
	note(880, 500)
	note(880, 500)
	note(698.5, 376)
	note(1046.5, 200)
	note(880, 500)
	note(698.5, 376)
	note(1046.5, 200)
	note(880, 1000)

	note(1318.5, 500)
	note(1318.5, 500)
	note(1318.5, 500)
	note(1397, 376)
	note(1046.5, 200)
	note(831, 500)
	note(698.5, 376)
	note(1046.5, 200)
	note(880, 1000)

if __name__ == "__main__":
        main()

