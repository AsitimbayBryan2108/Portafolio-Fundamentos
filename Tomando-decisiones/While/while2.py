#Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
#Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

p=0
n=int(input("Número (0 para terminar): "))
while n!=0:
    if n>0:
        p+=1
    n=int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", p)
