"""
En una avenida el límite es de 60 km/h. Si se excede hasta por 20 km/h, la multa es de $500. Si se excede 
por más de 20 km/h, la multa es de $1,000. Se necesita mostrar la multa a partir de la velocidad del 
vehículo. 
"""

def leerVelocidad():
    velocidad = int(input("Ingrese la velocidad del vehículo (km/h): "))
    return velocidad

def calcularMulta(velocidad):
    if velocidad <= 60:
        return 0
    elif velocidad <= 80:
        return 500
    else:
        return 1000

def mostrarMulta(multa):
    if multa == 0:
        print("No hay multa.")
    else:
        print(f"La multa es: ${multa}")
