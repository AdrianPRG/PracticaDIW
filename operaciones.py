def sumar(num1,num2):
    if(type(num1)==int and type(num2)==int or type(num1)==float and type(num2==float)):
        print("La suma es" ,  (num1+num2))
    else:
       print("Alguno no es entero")

def restar(num1,num2):
    if(type(num1)==int and type(num2)==int or type(num1)==float and type(num2==float)):
        print("La resta es" ,  (num1-num2))
    else:
       print("Alguno no es entero")

def multiplicacion(num1,num2):
    resultado = 0
    if(type(num1)==int and type(num2)==int or type(num1)==float and type(num2==float)):
        for i in range(0,num2):
            resultado = resultado + num1
        print("La multiplicacion es ", resultado)
    else:
       print("Alguno no es entero")

def dividir(num1, num2):
    cociente = 0
    for _ in range(int(num1)): 
        if num1 >= num2:
            num1 -= num2
            cociente += 1
    print("La división es:", cociente)

