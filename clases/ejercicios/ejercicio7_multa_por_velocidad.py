"""
En una avenida el límite es de 60 km/h. Si se excede hasta por 20 km/h, la multa es de $500. Si se excede 
por más de 20 km/h, la multa es de $1,000. Se necesita mostrar la multa a partir de la velocidad del 
vehículo. 
"""
#Agrega CLASE: define el nombre y la responsabilidad de una única clase. 
#Agrega ATRIBUTOS: especifica nombre, tipo, propósito y valor inicial de los datos que mantendrá el objeto. 
#Sustituye CONTRATO DE FUNCIONES por CONTRATO DE CLASE: incluye __init__ y los métodos necesarios, indicando qué hace cada uno. 
#Adapta ALGORITMO para usar atributos (self.atributo) y métodos; describe también cómo el menú crea y utiliza el objeto. 
#Utiliza self


class MultaVelocidad(object):
    def __init__(self):
        self.velocidad = 0
        self.multa = 0

    def leerVelocidad(self):
        self.velocidad = int(input("Ingrese la velocidad del vehículo (km/h): "))

    def calcularMulta(self):
        if self.velocidad > 60:
            if self.velocidad <= 80:
                self.multa = 500
            else:
                self.multa = 1000

    def mostrarMulta(self):
        if self.multa > 0:
            print(f"La multa a pagar es: ${self.multa}")
        else:
            print("No hay multa.")
