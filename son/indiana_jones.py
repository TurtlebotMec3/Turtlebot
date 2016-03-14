import kobuki_serial
import time

robot = kobuki_serial.Kobuki('/dev/kobuki')
a = 0.00000275

def note(f, t=500):
        global robot
        global a
        for i in range (0, t/200):
                robot.send([kobuki_serial.BuildRequestData.sound(int(1./(f*a)), 254)])
                time.sleep(0.1)
        time.sleep(0.2)

def main():
        note(659,750)
	note(698.5,250)
	note(784,1000)
	note(1046.5,2000)
	note(587,750)
	note(659,250)
	note(698.5,2000)
	note(784,750)
	note(880,250)
	note(988,1000)
	note(1397,2000)
	note(880,750)
	note(988,250)
	note(1046.5,1000)
	note(1175,1000)
	note(1318.5,1000)
	note(659,750)
	note(698.5,250)
	note(784,1000)
	note(1046.5,2000)
	note(1175,750)
	note(1318.5,250)
	note(1397,3000)

if __name__ == "__main__":
        main()

