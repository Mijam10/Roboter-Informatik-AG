#die Klasse des Server ist in Server.main
from Server.main import BefehlsServer

#intizalieisiert den Server
server = BefehlsServer()

#Starte den Server/das Programm laüft weiter wärend der Server an ist
server.start()

#Ändert die Geschwindigkeit 0-10 ist nach forne und 0-(-10) nach hinten
server.setF(-1)
#änder die Geschwindigkeit zur seite -10 ist nach Links und 10 nach rechts
server.setS(3)
# Um auf die befehle zu zu greifen muss der Ordenr Serve Eingefügt werden