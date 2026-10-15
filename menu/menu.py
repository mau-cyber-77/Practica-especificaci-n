from ejercicios import ejercicio1_luz as ej1 
from ejercicios import ejercicio2_calificacion as ej2 
from ejercicios import ejercicio3_compra as ej3 
from ejercicios import ejercicio4_estacionamiento as ej4 
from ejercicios import ejercicio5_renta_de_bicicletas as ej5
from ejercicios import ejercicio6_boleto_de_cine as ej6
from ejercicios import ejercicio7_multa_por_velocidad as ej7

def ejecutarEjercicio1(): 
    consumo= leerconsumo()
    pago=alcularPago(consumo)
    recibo=mostrarRecibo(consumo, pago)

def ejecutarEjercicio2(): 
    parciales = leerParciales()
    calificacion = calcularFinal(parciales)
    sin_reprobadas = verificarParciales(parciales)
    estado = determinarEstado(calificacion, sin_reprobadas)
    

def ejecutarEjercicio3(): 
    subtotal=leerSubtotal()
    descuento=calcularDescuento(subtotal)
    total=subtotal-descuento
    iva=calcularIVA(total)
    total= mostrarTotal(subtotal, descuento, iva, total)

def ejecutarEjercicio4(): 
    tiempo= leerMinutos()
    cobro= calcularCobro(tiempo)
    cobro= mostrarCobro(cobro)


def ejecutarEjercicio5(): 
    horas = leerHoras()
    renta = calcularRenta(horas)
    renta= mostrarRenta(renta)


def ejecutarEjercicio6():
    edad= leerEdad()
    precio= calcularPrecio(edad)
    precio= mostrarPrecio(precio)


def ejecutarEjercicio7():
    velocidad = leerVelocidad()
    multa = calcularMulta(velocidad)
    multa= mostrarMulta(multa)

def mostrarMenu(): 
    print() 
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Recibo de luz") 
    print("2. Calificación final") 
    print("3. Total de compra") 
    print("4. Estacionamiento") 
    print("5. Renta de bicicletas")
    print("6. Boleto de cine")
    print("7. Multa por velocidad")
    print("0. Salir") 

def menus(): 
    opcion = "" 
    while opcion != "0": 
        mostrarMenu() 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            ejecutarEjercicio1() 
        elif opcion == "2": 
            ejecutarEjercicio2() 
        elif opcion == "3": 
            ejecutarEjercicio3() 
        elif opcion == "4": 
            ejecutarEjercicio4() 
        elif opcion == "5":
            ejecutarEjercicio5()
        elif opcion == "6":
            ejecutarEjercicio6()
        elif opcion == "7":
            ejecutarEjercicio7()
        elif opcion != "0":
            print("Opción no válida.")

