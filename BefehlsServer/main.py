#die Klasse des Server ist in Server.main
from Server.main import BefehlsServer

#intizalieisiert den Server
server = BefehlsServer()

#Starte den Server/das Programm laüft weiter wärend der Server an ist
server.start()

#Ändert den Comand sonderzeichen funktionieren nicht so ganz
server.setCommand("Vorwaerts")
# Um auf die befehle zu zu greifen muss der Ordenr Serve Eingefügt werden