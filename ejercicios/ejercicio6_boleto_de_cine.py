"""
Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos de 60 años o más pagan la mitad. 
Se necesita mostrar el precio del boleto según la edad.

"""

def leerEdad():
    edad = int(input("Ingrese la edad del cliente: "))
    return edad

def calcularPrecio(edad):
    if edad <= 12 or edad >= 60:
        return 80 * 0.5  # Precio con descuento
    return 80

def mostrarPrecio(precio):
    print(f"El precio del boleto es: ${precio:.2f}")
