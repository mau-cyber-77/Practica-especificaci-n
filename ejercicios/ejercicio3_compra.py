"""
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de 
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket con 
subtotal, descuento, IVA y total.

"""

def leerSubtotal():
    subtotal = float(input("Ingrese el subtotal de la compra: "))
    return subtotal

def calcularDescuento(subtotal):
    if subtotal >= 5000:
        return subtotal * 0.2
    elif subtotal >= 1000:
        return subtotal * 0.1
    return 0

def calcularIVA(total):
    return total * 0.16

def mostrarTotal(subtotal, descuento, iva, total):
    print("----- TICKET -----")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")
    print("------------------")



