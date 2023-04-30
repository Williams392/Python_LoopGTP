# -*- coding: utf-8 -*-

def dispensadorDetallado(monto):
    lista = []
    billetes = [200,100,50,20,10]
    idx=0
    while(monto>0 and idx < len(billetes)):
        while(monto >= billetes[idx]):
            monto = monto - billetes[idx]
            lista.append(billetes[idx])
        idx = idx + 1
    return lista

def dispensadorAgrupado(monto):
    lista = []
    billetes = [200,100,50,20,10]
    idx=0
    
    while(monto>0 and idx < len(billetes)):       
     c = 0
     while(monto>=billetes[idx]):
         c+=1
         monto=monto-billetes[idx]         
    if(c>0):
        lista.append([billetes[idx],c])      
    idx = idx + 1   
    return lista


monto = int(input("Ingrese monto: "))
listaBi11 = dispensadorDetallado(monto)
print(listaBi11)

listaBi11Agr = dispensadorAgrupado(monto)
print(listaBi11Agr)


