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
        note(698.5,500)
	note(784,500)
	note(880,500)
	note(784,6*500)
	note(1,500)
	note(880,500 )
	note(880,500 )
	note(784,500)
	note(880,500)
	note(1,1000)
	note(698.5,500)
	note(784,500)
	note(698.5,250)
	note(1,250)
	note(698.5,1000)
	note(587,500)
	note(698.5,500)
	note(587,500)
	note(523,500)
	note(587,500)
	note(659,500)
	note(659,500)
	note(659,500)
	note(659,500)
	

if __name__ == "__main__":
        main()

