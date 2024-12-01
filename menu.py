#Importacion
from operaciones import sumar, restar, multiplicacion,dividir,factorial_recursivo

def mostrarmenu():
    print("Que desea: \n 1. Sumar numeros \n 2.Restar \n 3.Multiplicar \n 4.Dividir \n 5. Salir")
    numero = 0
    while(numero!=5):
        numero = int(input("Introduce un numero -> "))
        if(numero==1):
            print("Ha seleccionado sumar")
            sumar(pedirvalor1(),pedirvalor2())
        elif(numero==2):
            print("Ha seleccionado restar")
            restar(pedirvalor1(),pedirvalor2())
        elif(numero==3):
            print("Ha seleccionado multiplicar")
            multiplicacion(pedirvalor1(),pedirvalor2())
        elif(numero==4):
            print("Ha seleccionado dividir")
            dividir(pedirvalor1(),pedirvalor2())
        elif(numero==5):
            print("Saliendo del programa5")
        elif(numero==6):
            print("Ha seleccionado factorial recursivo")
            factorial_recursivo(pedirvalor1())
        else:
            print("Numero no registrado ")

def pedirvalor1():
    numero1 = input("Introduce numero 1 ")
    return numero1

def pedirvalor2():
    numero2 = input("Introduce numero 2 ")
    return numero2

mostrarmenu()