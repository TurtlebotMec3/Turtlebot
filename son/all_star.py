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
        note(784, 1000)
	note(1175, 500)
	note(988, 500)
	note(988, 1000)
	note(880, 250)
	note(784, 250)
	note(784, 250)
	note(1046.5,250)
	note(1046.5,250)
	note(988,250)
	note(988, 250)
	note(880, 250)
	note(880,500 )
	note(784,500)
	note(0, 500)
	note(784,500 )
	note(1175,250)
	note(988,250)
	note(988,250 )
	note(880, 250)
	note(880, 250)
	note(784, 250)
	note(784, 250)
	note(659, 250)
	note(659, 250)
	note(587, 750)

if __name__ == "__main__":
        main()

