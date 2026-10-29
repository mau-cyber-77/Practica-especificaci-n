from clases.ejemplo.calculadora import Calculadora
from clases.ejercicios.ejercicio1_luz import Ejercicio1Luz
from clases.ejercicios.ejercicio2_calificacion import Ejercicio2Calificacion

class Menu(object):
    def __init__(self):
        self.opcion = 0

    def mostrarMenu(self):
        print()
        print("Ejemplo programacion orientada a objetos:")
        print("1. Calculadora")
        print("2. Recibo de luz")
        print("3. Calificacion Final")
        print("0. Salir")
      

    def menu(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrarMenu()
            self.opcion = input("Seleccione una opción: ")
            if self.opcion == "1":
                casio = Calculadora()
                casio.leerNumeros()
                casio.calcularSuma()
                casio.mostrarSuma()

            elif self.opcion == "2":
                CFE = Ejercicio1Luz()
                CFE.leerconsumo()
                CFE.calcularPago()
                CFE.mostrarRecibo()
            
            elif self.opcion == "3":
                escuela = Ejercicio2Calificacion()
                escuela.leerParciales
                escuela.calcularCalificacionFinal
                escuela.determinarEstado
                escuela.mostrarResultado

            else:
                print("Opción no válida.")
