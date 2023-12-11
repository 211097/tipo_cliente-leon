from my_first_package.cliente import Cliente, ClienteBronce, ClientePlata
from datetime import datetime
#cliente normales
#Vegeta = Cliente("001", "vegeta", "777", 30)
#Auron = Cliente("002", "Auron", "Play", 50)

#print(Vegeta)
#print(Auron)

# Ejemplo de uso:
cliente_bronce_juan = ClienteBronce("003", "Juan", "Perez", 30, "1234567890")
print(cliente_bronce_juan)  # Imprimirá: 001 Juan Perez 30 1234567890
print(" ")
cliente_bronce_juan.imprimir_ticket(150, datetime.now())
cliente_bronce_juan.apartar_producto("Producto lavadora")

cliente_plata_maria = ClientePlata("004", "Maria", "Gomez", 25, "0987654321", "maria@example.com")
print(cliente_plata_maria)  # Imprimirá: 002 Maria Gomez 25 0987654321 maria@example.com
print(" ")
cliente_plata_maria.imprimir_ticket(200, datetime.now())
cliente_plata_maria.apartar_producto("Producto bicicleta")







