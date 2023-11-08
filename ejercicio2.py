"""Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir."""

def main():
    nombre=input("Introduzca su nombre: ");
    edad=int(input(f"Introduzca su edad {nombre}: "))
    edad = input("Hola, " + nombre + ". Por favor, introduce tu edad: ") 

    # Convertir la entrada de edad a un número entero 

    edad = int(edad) 

    # Comprobar si la persona es mayor de 18 años 

    if edad >= 18: 

        print("¡Hola, " + nombre + "! Ya puedes conducir.") 

    else: 

        print("Lo siento, " + nombre + ". Debes ser mayor de 18 años para poder conducir.") 

if __name__== "__main__" :
    main()
