def sumar(num1,num2):
    try:
        print("La suma es " , float(num1) + float(num2))
    except ValueError:
        print("Algun elemento no es numerico")

def restar(num1,num2):
    try:
        print("La resta es " , float(num1) - float(num2))
    except ValueError:
        print("Algun elemento no es numerico")

def multiplicacion(num1,num2):
    resultado = 0.0
    try:
        for i in range(0,int(num2)):
            resultado = resultado + float(num1)
        print("La multiplicacion es", resultado)
    except ValueError:
        print("Algun elemento no es numerico")

def dividir(num1, num2):
    try:
        cociente = 0.0
        num1 = float(num1)
        num2 = float(num2)
        for x in range(int(num1)): 
            if num1 >= num2:
                num1 -= num2
                cociente += 1.0
        print("La división es:", cociente)
    except ValueError:
        print("Algun elemento no es numerico")
   
