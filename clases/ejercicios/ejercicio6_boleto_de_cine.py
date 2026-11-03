"""
Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos de 60 años o más pagan la mitad. 
Se necesita mostrar el precio del boleto según la edad.
"""
#Agrega CLASE: define el nombre y la responsabilidad de una única clase. 
#Agrega ATRIBUTOS: especifica nombre, tipo, propósito y valor inicial de los datos que mantendrá el objeto. 
#Sustituye CONTRATO DE FUNCIONES por CONTRATO DE CLASE: incluye __init__ y los métodos necesarios, indicando qué hace cada uno. 
#Adapta ALGORITMO para usar atributos (self.atributo) y métodos; describe también cómo el menú crea y utiliza el objeto. 
#Utiliza self

class BoletoCine(object):
    def __init__(self):
        self.edad = 0
        self.precio = 80

    def leerEdad(self):
        self.edad = int(input("Ingrese la edad del espectador: "))

    def calcularPrecio(self):
        if self.edad <= 12 or self.edad >= 60:
            self.precio *= 0.5  # Aplicar 50% de descuento

    def mostrarPrecio(self):
        print(f"El precio del boleto es: ${self.precio:.2f}")
