from operaciones import sumar, restar, multiplicacion

def mostrarmenu():
    print("Que desea: \n 1. Sumar numeros \n 2.Restar \n 3.Multiplicar \n 4.Dividir \n 5. Salir")
    numero = int(input("Introduce un numero"))
    while(numero!=5):
        numero = int(input("Introduce un numero"))
        if(numero==1):
            sumar(pedirvalor1(),pedirvalor2())
        elif(numero==2):
            restar(pedirvalor1(),pedirvalor2())
        elif(numero==3):
            multiplicacion(pedirvalor1(),pedirvalor2())
        else:
            print("Numero no registrado")

def pedirvalor1():
    numero1 = input("Introduce numero 1")
    return numero1

def pedirvalor2():
    numero2 = input("Introduce numero 2")
    return numero2