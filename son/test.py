import kobuki_serial
import time

robot = kobuki_serial.Kobuki('/dev/kobuki')
a = 0.00000275

def note(f, t=500):
        global robot
        global a
        for i in range (0, t/200):
                robot.send([kobuki_serial.BuildRequestData.sound(int(1./(f*a)), 125)])
                time.sleep(0.1)
        time.sleep(0.1)

def main():
        note(659,600)
	note(698.5,200)
	note(784,800)
	note(1046.5,1600)
	note(587,600)
	note(659,200)
	note(698.5,1600)
	note(784,600)
	note(880,200)
	note(988,800)
	note(1397,1600)
	note(880,600)
	note(988,200)
	note(1046.5,800)
	note(1175,800)
	note(1318.5,800)
	note(659,600)
	note(698.5,200)
	note(784,800)
	note(1046.5,1600)
	note(1175,600)
	note(1318.5,200)
	note(1397,2400)

if __name__ == "__main__":
        main()

