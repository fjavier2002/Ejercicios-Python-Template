# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.

# Implemente función esMayorEdad(e)

def esMayorEdad(edad): 

    return edad >= 18 
# Programa principal
def main():
    nombre="Mariano"
    edad=0

    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...
    if esMayorEdad(edad): 

        print("¡Hola, " + nombre + "! Ya puedes conducir.") 

    else: 

        print("Lo siento, " + nombre + ". Debes ser mayor de 18 años para poder conducir.") 
if __name__== "__main__" :
   main()
