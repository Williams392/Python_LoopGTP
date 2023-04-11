# Declaración de variables globales
facturas_mayor_300 = 0
suma_ventas = 0
max_cant_frutas = 0
facturas_una_fruta = 0

def generar_factura():
    # Uso de variables globales
    global facturas_mayor_300, suma_ventas, max_cant_frutas, facturas_una_fruta
    
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cant_frutas = int(input("Ingrese la cantidad de tipos de frutas a comprar: "))
    frutas = {}
    total = 0
    
    for i in range(cant_frutas):
        nombre_fruta = input("Ingrese el nombre de la fruta: ")
        cant_fruta = int(input("Ingrese la cantidad de " + nombre_fruta + " a vender: "))
        precio_fruta = float(input("Ingrese el precio unitario de " + nombre_fruta + " en soles: "))
        frutas[nombre_fruta] = {'cantidad': cant_fruta, 'precio': precio_fruta}
        total += cant_fruta * precio_fruta
    
    print("Factura de", nombre_cliente)
    for fruta in frutas:
        print(fruta, "-", frutas[fruta]['cantidad'], "unidades a", frutas[fruta]['precio'], "soles cada una")
    print("Total de la venta:", total, "soles")
    
    # Actualización de variables globales
    if total >= 300:
        facturas_mayor_300 += 1
        
    suma_ventas += total
    
    cant_frutas = len(frutas)
    if cant_frutas > max_cant_frutas:
        max_cant_frutas = cant_frutas
        
    if cant_frutas == 1:
        facturas_una_fruta += 1
    
    return total

# Ciclo principal
while True:
    generar = input("¿Desea generar una factura? (s/n): ")
    if generar.lower() == 'n':
        break
        
    total_venta = generar_factura()
    
# Resumen
print("Resumen de ventas:")
print("- Cantidad de facturas con un monto de venta mayor igual a S/300:", facturas_mayor_300)
print("- Promedio de ventas de las facturas en soles:", suma_ventas/(facturas_mayor_300+1))
print("- Máxima cantidad de frutas vendidas en una factura:", max_cant_frutas)
print("- Cantidad de facturas con un solo tipo de frutas:", facturas_una_fruta)

# Prueba
print("Prueba de ingreso de 3 facturas:")
for i in range(3):
    print("Factura", i+1)
    generar_factura()
