n = int(input("Ingrese la cantidad de valores: ")) 

valores = []
for i in range(n):
    valor = int(input(f"Ingrese el valor {i+1}: ")) # posicion 
    valores.append(valor)

multiplo3 = []
sumaMultiplo3 = 0

# verificar
for valor in valores:
    if valor % 3 == 0:
        multiplo3.append(valor)
        sumaMultiplo3 += valor

if len(multiplo3) > 0:
    print("Los valores múltiplos de 3 son:", multiplo3)
    print("La sumatoria de los múltiplos de 3 es:", sumaMultiplo3)
else:
    print("No hay valores múltiplos de 3 en la lista ingresada.")
    


