import socket
import time
def setServo( servo, grad):

    try:
        if int(grad) < 0:
            grad = 0
        elif int(grad) > 360:
            grad = 360
        prozent = (int(grad) / 90) * 10 + 10
        command = str(servo) + ":" + str(prozent)
        print(command)
        msg = command.encode('ascii')
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("raspberrypi", 2255))
            s.send(msg)
        except:
            print("Conection error")
    except:
            print("FalscheEingabe")
class Roboter:
    def __init__(self):
        self.servos = []
        for i in range(0,8):
            self.servos.append([i,20])
    def moveY(self):
        for i in [1,3,5,7]:
            setServo(i,0)
            setServo(i+1,180)
            time.sleep(1)
            setServo(i+1,90)
            time.sleep(1)
        for i in [1,3,5,7]:
            setServo(i, 180)
rasp = Roboter()
rasp.moveY()


