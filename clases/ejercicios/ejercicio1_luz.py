class Ejercicio1Luz(object):
   def __init__(self):
       self.luz = 0

   def leerconsumo(self):
       self.luz = float(input("Ingrese el consumo mensual en kWh: "))

   def calcularPago(self):
       if self.luz <= 150:
           total = self.luz * 1.00
       elif self.luz <= 280:
           total = 150 * 1.00 + (self.luz - 150) * 1.50
       else:
           total = 150 * 1.00 + 130 * 1.50 + (self.luz - 280) * 3.00
       return total

   def mostrarRecibo(self):
       total = self.calcularPago()
       print(f"El importe del recibo es: ${total:.2f}")

