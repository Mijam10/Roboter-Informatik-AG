import socket
def getCommand(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 2255))
    msg = (s.recv(1024).decode('ascii')).split()
    return msg
#Dammit kann man vom raspberry den befehl einholen C6H12O6 muss aber mit dem namen des empfängers angegeben werden
print(getCommand("C6H12O6"))