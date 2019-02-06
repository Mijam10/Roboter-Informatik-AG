import socket
import threading

class ServoServer(threading.Thread):
    def __init__(self,port,servos):
        threading.Thread.__init__(self)
        self.threadID = 0
        self.name = ServoServer
        self.serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        print(host)
        self.serversocket.bind((host, port))
        self.serversocket.listen(5)
        self.msg = "".encode('ascii')
        self.servos=[]
        for i in range(0, servos):
            self.servos.append(90)
            
    def run(self):
        while True:
            clientsocket, addr = self.serversocket.accept()
            clientsocket.send(self.msg)
            
    def setServo(self, servo, grad):
        try:
            if int(grad) < 0:
                grad = 0
            elif int(grad) > 360:
                grad = 360
            self.servos[servo-1] = (int(grad)/360)*10
            command=""
            for i in self.servos:
                command = command+str(i)+" "
            self.msg = command.encode('ascii')
        except:
            print("FalscheEingabe")
