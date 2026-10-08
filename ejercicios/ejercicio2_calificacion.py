"""
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó.
"""

def leer_parciales():
    parciales = []
    for i in range(1, 4):
        parcial = float(input(f"Ingrese la calificación del parcial {i}: "))
        parciales.append(parcial)
    return parciales

def calcular_calificacion_final(parciales):
    if any(p < 50 for p in parciales):
        return 0
    return sum(p * w for p, w in zip(parciales, [0.3, 0.3, 0.4]))

def determinar_estado(calificacion_final):
    if calificacion_final >= 70:
        return "aprobó"
    else:
        return "reprobó"



def mostrar_resultados(calificacion_final):
    estado = determinar_estado(calificacion_final)  
    if calificacion_final == 0:
        print("El alumno reprobó la materia.")
    else:
        print(f"La calificación final es: {calificacion_final:.2f}")
        if calificacion_final >= 70:
            print("El alumno aprobó la materia.")
        else:
            print("El alumno reprobó la materia.")
