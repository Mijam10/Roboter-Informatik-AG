import socket
import threading
class ServoServer(threading.Thread):
    def __init__(self,port):
        threading.Thread.__init__(self)
        self.threadID = 0
        self.name = ServoServer
        self.serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        self.serversocket.bind((host, port))
        self.serversocket.listen(5)
        self.msg = "".encode('ascii')
        self.x = 0
        self.y = 0
    def run(self):
        while True:
            clientsocket, addr = self.serversocket.accept()

            clientsocket.send(self.msg)
    def setCommand(self,command):
        try:
            command=str(command)
            self.msg = command.encode('ascii')
        except:
            print("FalscheEingabe")
    def setF(self,x):
        try:
            self.x = int(x)
            command = str(self.x)+" "+str(self.y)
            self.msg = command.encode('ascii')
        except:
            print("FalscheEingabe")
    def setS(self,y):
        try:
            self.y = int(y)
            command = str(self.x)+" "+str(self.y)
            self.msg = command.encode('ascii')
        except:
            print("FalscheEingabe")
