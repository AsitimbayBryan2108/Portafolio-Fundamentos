#Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
#Finalmente, mostrar la sumatoria de todos los números ingresados.

t=0
n=int(input("Número: "))
while n != 0:
    t+=n
    n=int(input("Número: "))
