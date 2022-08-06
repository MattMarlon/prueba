""" ingresar una lista por teclado solo de numero positivos si
se ingresa un numero negativo se detendra el llenado de la lista
y me imprima el cuadrado de un numero ingresado por teclado
"""
print("si se introduce un numero negativo se\ndetendra el llenado de la lista")
n=1
while(n>0):
    n=int(input("ingrese un numero diferente de cero: "))
    
print("se procedera a calcular el cuadrado de un número\ningresado por teclado")
    
x=int(input("ingrese un numero: "))
cuadrado= x**x
print("el cuadrado del numero ingresado es: ",cuadrado)
