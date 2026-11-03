"""
Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más, se aplica un 15% de descuento. Se 
necesita mostrar el importe a pagar según las horas de renta. 
"""
#Agrega CLASE: define el nombre y la responsabilidad de una única clase. 
#Agrega ATRIBUTOS: especifica nombre, tipo, propósito y valor inicial de los datos que mantendrá el objeto. 
#Sustituye CONTRATO DE FUNCIONES por CONTRATO DE CLASE: incluye __init__ y los métodos necesarios, indicando qué hace cada uno. 
#Adapta ALGORITMO para usar atributos (self.atributo) y métodos; describe también cómo el menú crea y utiliza el objeto. 
#Utiliza self

class RentaBicicletas(object):
    def __init__(self):
        self.horas = 0
        self.renta = 0.0

    def leerHoras(self):
        self.horas = int(input("Ingrese el número de horas de renta: "))

    def calcularRenta(self):
        self.renta = self.horas * 30
        if self.horas >= 3:
            self.renta *= 0.85  # Aplicar 15% de descuento

    def mostrarRenta(self):
        print(f"El importe a pagar es: ${self.renta:.2f}")

