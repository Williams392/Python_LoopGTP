# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -----------------------------------

print("hello word")


# -----------------------------------

x = range(1,10,5)

for n in x:
    print(n)

# ---------------------

# int correctas, incorrectas, blanco, puntos;


print()
#print("Ingresa el número de respuestas correctas: ")
correctas = int(input("Ingresa el número de respuestas correctas: "))

#print("Ingresa el número de respuestas incorrectas: ")
incorrectas = int(input("Ingresa el número de respuestas incorrectas: "))

#print("Ingresa el número de respuestas en blanco: ")
blanco = int(input("Ingresa el número de respuestas en blanco: "))

puntos = (correctas * 4) + (incorrectas * (-1))  

print("El puntaje final es", puntos)
print()

