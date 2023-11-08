# coding=utf-8
__Author__="Fº Javier Cerá"

import random

# Función que determina si un numero es par.

def esPar(numero) :
    if numero % 2 == 0:
        return True
    else:
        return False # --> Implemente código de la función <--

def esImpar(numero) :
    if numero % 2 == 0:
        return False
    else:
        return True # --> Implemente código de la función <--

def generarPares(valores, inicio) :
    pares=[]
    numero=inicio
    if esImpar(inicio) :
        numero=inicio+1
    # --> Complete código de la función <--

    while len(pares) < valores:
        pares.append(numero)
        numero += 2
    return pares

def generarImpares(valores, inicio) :
    impares=[]
    numero=inicio
    numero = inicio + 1
    if esImpar(inicio) :
        numero=inicio

    # --> Complete código de la función <--
    while len(impares) < valores:
        impares.append(numero)
        numero += 2
    return impares

# Programa principal
def main():
    print("Par e impar")
    n=int(input("Introduzca un numero: "))
    print("{0} es par --> {1}.".format(n,esPar(n)))
    m=int(input("Introduzca el número de valores: "))
    i=int(input("Introduzca el número inicial: "))
    x=generarPares(m,i)
    y=generarImpares(m,i)
    print("Impares: ",y)
    print("Pares: ",x)    

if __name__== "__main__" :
   main()
