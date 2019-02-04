import socket
def grad(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    msg = (s.recv(1024).decode('ascii')).split()
    return msg
#Dammit kann man vom raspberry den befehl einholen C6H12O6 muss aber mit dem namen des empfängers angegeben werden und dem port
print(grad("C6H12O6", 2255))
print(grad("C6H12O6", 2256))
print(grad("C6H12O6", 2257))
print(grad("C6H12O6", 2258))