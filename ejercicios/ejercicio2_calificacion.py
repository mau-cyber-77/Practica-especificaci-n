"""
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y 
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia. Se 
necesita mostrar la calificación final y si el alumno aprobó.
"""


def leerParciales():
    parciales = []
    for i in range(3):
        parcial = float(input(f"Ingrese la calificación del parcial {i + 1}: "))
        parciales.append(parcial)
    return parciales

def calcularCalificacionFinal(parciales):
    calificacion_final = (parciales[0] * 0.3) + (parciales[1] * 0.3) + (parciales[2] * 0.4)
    return calificacion_final

def verificarParciales(parciales):
    for parcial in parciales:
        if parcial < 50:
            return False
    return True

def determinarEstado(calificacion_final):
    if not sin_reprobadas:
        return "reprobo (tiene un parcial menor a 50)"
    elif calificacion_final >= 70:
        return "aprobo"
    else:
        return "reprobo (calificación final menor a 70)"



    



