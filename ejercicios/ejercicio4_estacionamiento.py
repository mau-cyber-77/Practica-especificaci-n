"""
Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o fracción. 
El cobro máximo es de $150. El sistema recibe el tiempo de estancia en minutos y 
muestra el importe a cobrar. 

Condición adicional: la especificación debe decir de forma explícita cómo se redondea la 
fracción y si se permite o no usar módulos de la biblioteca estándar de Python. Se verifica que 
Copilot respete esa decisión. 
"""

def leerMinutos():
    tiempo = int(input("Ingrese el tiempo de estancia en minutos: "))
    return tiempo

def calcularCobro(tiempo):
    horas = tiempo / 60
    if horas <= 1:
        cobro = 20
    else:
        cobro = 20 + (horas - 1) * 15
    if cobro > 150:
        cobro = 150
    return cobro

def mostrarCobro(cobro):
    print(f"El importe a cobrar es: ${cobro:.2f}")
