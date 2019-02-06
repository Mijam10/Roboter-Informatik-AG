import socket
def grad(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        msg = (s.recv(1024).decode('ascii')).split()
        return msg
    except:
        print("Connerction Error")
        return [90,90,90,90,90,90,90,90]
#Dammit kann man vom raspberry den befehl einholen C6H12O6 muss aber mit dem namen des empfängers angegeben werden und dem port
while 1:
    print(grad("Lenovo-PC", 2255))
