totalVentas = 0
facturaMayor_300 = 0
maxCantidadFrutas = 0
unSoloTipoFruta = 0

class Factura:
    def __init__(self, cliente):
        self.cliente = cliente
        self.frutas = []
        self.total = 0

    def agregar_fruta(self, nombre, cantidad, precio):
        self.frutas.append((nombre, cantidad, precio))
        self.total += cantidad * precio

    def imprimir_resumen(self):
        global totalVentas, facturaMayor_300, maxCantidadFrutas, unSoloTipoFruta

        totalVentas += self.total
        if self.total >= 300:
            facturaMayor_300 += 1
        cantidad_frutas = sum([cantidad for _, cantidad, _ in self.frutas])
        if cantidad_frutas > maxCantidadFrutas:
            maxCantidadFrutas = cantidad_frutas
        if len(set([nombre for nombre, _, _ in self.frutas])) == 1:
            unSoloTipoFruta += 1
        
        # Resumen de factura   
        print()
        print("=========================================")
        print("|      Factura de  Fruteria Kevin       |")
        print("=========================================")
        print(f" Resumen de factura para {self.cliente}: ")
        for nombre, cantidad, precio in self.frutas:
            print(f" {cantidad} x {nombre}: S/{precio:.2f} c/u ")
        print(f" Total: S/{self.total:.2f}")
        print("=========================================")
        print()
        

#  3 facturas
factura1 = Factura("Raul Iman")
factura1.agregar_fruta("Pera", 13, 1.5)
factura1.agregar_fruta("Platano", 3, 2.0)

factura2 = Factura("Nciole Baldeon")
factura2.agregar_fruta("Platanos", 5, 1.5)
factura2.agregar_fruta("naranja", 1, 2.5)
factura2.agregar_fruta("Naranjas", 2, 2.0)

factura3 = Factura("Juan Satnos")
factura3.agregar_fruta("Melon", 1, 10.0)
factura3.agregar_fruta("naranja", 2, 4.0)
factura3.agregar_fruta("Pera", 31, 4.0)

facturas = [factura1, factura2, factura3]

for factura in facturas:
    factura.imprimir_resumen()


facturas = []
while True:
    print()
    respuesta = input(" Desea generar una factura (Si/No): ")
    if respuesta.lower() == "n":
        break
    cliente = input(" Ingrese el nombre del cliente: ")
    numFrutas = int(input(" Cuantos tipos de frutas va a comprar: "))
    if numFrutas <= 0:
        print(" El número de frutas debe ser mayor que cero. Intente de nuevo.")
        continue
    factura = Factura(cliente)
    for i in range(numFrutas):
        nombre = input(f" Ingrese el nombre de la fruta, Solo {i+1} nombre: ")
        cantidad = int(input(f" Ingrese la cantidad de -> {nombre} a vender: "))
        precio = float(input(f" Ingrese el precio unitario de {nombre}: "))
        factura.agregar_fruta(nombre, cantidad, precio)
    facturas.append(factura)
    factura.imprimir_resumen()

promdVentas = totalVentas