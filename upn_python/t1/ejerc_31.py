totalVentas = 0
facturaMayor_300 = 0
promdVentas = 0
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
        global totalVentas, facturaMayor_300, promdVentas, maxCantidadFrutas, unSoloTipoFruta
        # Actualizar variables globales
        totalVentas += self.total
        if self.total >= 300:
            facturaMayor_300 += 1
        promdVentas = totalVentas / len(facturas)
        cantidad_frutas = sum([cantidad for _, cantidad, _ in self.frutas])
        if cantidad_frutas > maxCantidadFrutas:
            maxCantidadFrutas = cantidad_frutas
        if len(set([nombre for nombre, _, _ in self.frutas])) == 1:
            unSoloTipoFruta += 1
        
        # Imprimir resumen de factura   
        print()
        print(f"Resumen de factura para {self.cliente}:")
        for nombre, cantidad, precio in self.frutas:
            print(f"{cantidad} x {nombre}: S/{precio:.2f} c/u")
        print(f"Total: S/{self.total:.2f}\n")

facturas = []
while True:
    respuesta = input("¿Desea generar una factura? (S/N) ")
    if respuesta.lower() == "n":
        break
    cliente = input("Ingrese el nombre del cliente: ")
    num_frutas = int(input("Cuantos tipos de frutas va a comprar: "))
    if num_frutas <= 0:
        print("El número de frutas debe ser mayor que cero. Intente de nuevo.")
        continue
    factura = Factura(cliente)
    for i in range(num_frutas):
        nombre = input(f"Ingrese el nombre de la fruta #{i+1}: ")
        cantidad = int(input(f"Ingrese la cantidad de {nombre} a vender: "))
        precio = float(input(f"Ingrese el precio unitario de {nombre}: "))
        factura.agregar_fruta(nombre, cantidad, precio)
    facturas.append(factura)
    if factura.total >= 300:
        facturaMayor_300 += 1
    promdVentas = totalVentas / len(facturas)
    if factura.total > maxCantidadFrutas:
        maxCantidadFrutas = factura.total
    if len(set([nombre for nombre, _, _ in factura.frutas])) == 1:
        unSoloTipoFruta += 1
    factura.imprimir_resumen()

# Imprimir resumen final
print()
print(f"Cantidad de facturas con un monto de venta mayor igual a S/300: {facturaMayor_300}")
print(f"Promedio de ventas de las facturas en soles: S/{promdVentas:.2f}")
print(f"Máxima cantidad de frutas vendidas en una factura: {maxCantidadFrutas}")
print(f"Cantidad de facturas con un solo tipo de frutas: {unSoloTipoFruta}")

