#die Klasse des Server ist in Server.main
from Server.server import ServoServer

#intizalieisiert den Server
B1 = ServoServer(2255)
B2 = ServoServer(2256)
B3 = ServoServer(2257)
B4 = ServoServer(2258)

#Starte den Server/das Programm laüft weiter wärend der Server an ist
B1.start()
B2.start()
B3.start()
B4.start()

#Ändert die Gradzahl am oberen Servo
B1.setF(-1)
B2.setF(-3)
B3.setF(-5)
B4.setF(-4)
#änder die Gradzahl am Unteren Servo
B1.setS(3)
# Um auf die befehle zu zu greifen muss der Ordenr Serve Eingefügt werden