#die Klasse des Server ist in Server.main
from Server.server import ServoServer

#intizalieisiert den Server
S1 = ServoServer(2255,8)


#Starte den Server/das Programm laüft weiter wärend der Server an ist
S1.start()


#Ändert die Gradzahl des angegeben Servo
S1.setServo(1,6)

while 1:
    try:
        i = input("Welcher Servo:Grad").split(":")
        print(i)
        S1.setServo(int(i[0]),int(i[1]))
    except:
        print("BadInput")