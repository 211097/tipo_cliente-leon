from datetime import datetime
#estructura para clientes
#aparte de los metodos init y str, tengo los metodos imprimir tiket y apartar producto
#aplico herecia al heredar los atributos de cliente a mis clases hijas cliente bronce y cliente plata
class Cliente:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellidos} {self.edad}"

    def imprimir_ticket(self, total, fecha_de_compra):
        print("Datos del Cliente:")
        print(self)
        print(f"Total: {total}")
        print(f"Fecha de compra: {fecha_de_compra}")
        print()

    def apartar_producto(self, nombre_producto):
        print("Datos del Cliente:")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"Producto apartado: {nombre_producto}")
        print()

#agrego numero_celular 
class ClienteBronce(Cliente):
    def __init__(self, id, nombre, apellidos, edad, numero_celular):
        super().__init__(id, nombre, apellidos, edad)
        self.numero_celular = numero_celular

    def __str__(self):
        return f"{super().__str__()} {self.numero_celular}"

    def imprimir_ticket(self, total, fecha_de_compra):
        super().imprimir_ticket(total, fecha_de_compra)
    
    def apartar_producto(self, nombre_producto):
        print("Cliente Bronce:")
        super().apartar_producto(nombre_producto)

#agrego numero_celular y correo_electronico al hacer esto aplico poliformismo
class ClientePlata(Cliente):
    def __init__(self, id, nombre, apellidos, edad, numero_celular, correo_electronico):
        super().__init__(id, nombre, apellidos, edad)
        self.numero_celular = numero_celular
        self.correo_electronico = correo_electronico

    def __str__(self):
        return f"{super().__str__()} {self.numero_celular} {self.correo_electronico}"

    def imprimir_ticket(self, total, fecha_de_compra):
        super().imprimir_ticket(total, fecha_de_compra)
    
    def apartar_producto(self, nombre_producto):
        print("Cliente Plata:")
        super().apartar_producto(nombre_producto)


