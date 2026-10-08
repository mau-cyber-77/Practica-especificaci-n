"""
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes. 
"""
def leerconsumo():
    consumo = float(input("Ingrese el consumo mensual en kWh: "))
    return consumo

def calcular_recibo(consumo):
    if consumo <= 150:
        total = consumo * 1.00
    elif consumo <= 280:
        total = 150 * 1.00 + (consumo - 150) * 1.50
    else:
        total = 150 * 1.00 + 130 * 1.50 + (consumo - 280) * 3.00
    return total

def mostrar_recibo(total):
    print(f"El importe del recibo es: ${total:.2f}")

