import socket
import threading
class BefehlsServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadID = 0
        self.name = BefehlsServer
        self.serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        self.serversocket.bind((host, 2255))
        self.serversocket.listen(5)
        self.command = "NoCommand"
        self.msg = "NoCommand".encode('ascii')
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