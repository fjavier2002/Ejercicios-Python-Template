# coding=utf-8
__Author__="Fº Javier Cerá"


# Función que determina si un numero es primo.

def esPrimo(numero) :
    contador = 0

    if numero==1 :
        return True

    # --> Implemente el código del Bucle <--
    for i in range(1, numero+1):
        if (numero % i) == 0:
            contador = contador + 1
    # Si tiene solo dos divisores el número es primo     
    if contador == 2 :
        return True
    else :
        return False

# Programa principal
def main():
    print("ES PRIMO")
    n=int(input("Introduzca un numero: "))
    print("{0} es primo --> {1}.".format(n,esPrimo(n)))

if __name__== "__main__" :
   main()
