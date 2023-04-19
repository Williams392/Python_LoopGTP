# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:01:54 2023

@author: PC
"""

print("hello word")

# 2 funciones para el ordenamiento:
# len -> para devolver la longiturd
    
def Ord_burbuja_menor(men):
    n = len(men)
    for i in range(n):
        for j in range(0, n-i-1):
            if men[j] > men[j+1]:
                men[j], men[j+1] = men[j+1], men[j]

                
def Ord_burbuja_mayor( may):
    n = len(may)
    for i in range(n):
        for j in range(0, n-i-1):
            if may[j] < may[j+1]:
                may[j], may[j+1] = may[j+1], may[j]



men = [4, 77, 18, 11, 27, 34, 100]

Ord_burbuja_menor(men)
print("\n Lista ordenada de menor a mayor: ")
for i in range(len(men)):
    print("%d" % men[i]),
    
    
may = [4, 77, 18, 11, 27, 34, 100]

Ord_burbuja_mayor(may)
print("\n Lista ordenada de mayor a menor: ")
for i in range(len(may)):
    print("%d" % may[i]),