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

# Lista de pruebas
pruebas = [
    ("Juan", 3, [("Manzana", 2, 2.5), ("Pera", 3, 1.75), ("Plátano", 1, 0.75)]),
    ("María", 2, [("Fresa", 5, 1.2), ("Uva", 1, 3.5)]),
    ("Pedro", 1, [("Mango", 2, 2.0)])
]

facturas = []
for prueba in pruebas:
    factura = Factura(prueba[0])
    for fruta in prueba[2]:
        factura.agregar_fruta(fruta[0], fruta[1], fruta[2])
    facturas.append(factura)
    factura.imprimir_resumen()

promdVentas = totalVentas
