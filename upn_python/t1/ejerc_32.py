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
        print(f" Total: S/{self.total:.2f} \n")
        print("=========================================")

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
