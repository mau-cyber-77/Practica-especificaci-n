from clases.ejemplo.calculadora import Calculadora
from clases.ejercicios.ejercicio1_luz import Ejercicio1Luz
from clases.ejercicios.ejercicio2_calificacion import Ejercicio2Calificacion
from clases.ejercicios.ejercicio5_renta_de_bicicletas import RentaBicicletas
from clases.ejercicios.ejercicio6_boleto_de_cine import BoletoCine
from clases.ejercicios.ejercicio7_multa_por_velocidad import MultaVelocidad


class Menu(object):
    def __init__(self):
        self.opcion = 0

    def mostrarMenu(self):
        print()
        print("Ejemplo programacion orientada a objetos:")
        print("1. Calculadora")
        print("2. Recibo de luz")
        print("3. Calificacion Final")
        print("4. Renta de bicicletas")
        print("5. Boleto de cine")
        print("6. Multa por exceso de velocidad")
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
                escuela.leerParciales()
                escuela.calcularCalificacionFinal()
                escuela.determinarEstado()
                escuela.mostrarResultado()

            elif self.opcion == "4":
                bicicleta = RentaBicicletas()
                bicicleta.leerHoras()
                bicicleta.calcularRenta()
                bicicleta.mostrarRenta()
            
            elif self.opcion == "5":
                boleto = BoletoCine()
                boleto.leerEdad()
                boleto.calcularPrecio()
                boleto.mostrarPrecio()
            
            elif self.opcion == "6":
                multa = MultaVelocidad()
                multa.leerVelocidad()
                multa.calcularMulta()
                multa.mostrarMulta()
            
            else:
                print("Opción no válida.")
