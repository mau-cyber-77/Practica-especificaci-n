"""
Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más, se aplica un 15% de descuento. Se 
necesita mostrar el importe a pagar según las horas de renta. 
"""

def leerHoras():
    horas = int(input("Ingrese el número de horas de renta: "))
    return horas

def calcularRenta(horas):
    renta = horas * 30
    if horas >= 3:
        renta *= 0.85  # Aplicar 15% de descuento
    return renta

def mostrarRenta(renta):
    print(f"El importe a pagar es: ${renta:.2f}")
