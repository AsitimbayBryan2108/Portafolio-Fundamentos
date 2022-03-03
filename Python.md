## ¿Qué es Python?
Python es un lenguaje sencillo de leer y escribir dada su gran similitud con el lenguaje humano, además es un lenguaje  de código abierto y por lo tanto libre y multiplataforma, lo que permite un desarrollo ilimitado de software.


   ![images-removebg-preview](https://user-images.githubusercontent.com/99736243/156488107-3f0082cc-d59e-47f6-b890-fa21367ef17b.png)


## ¿Qué es una variable?
Una variable es una declaracion para decirle al programa dónde comenzar, qué nombre tendrá y qué tipo de datos almacenará. Este es un elemento que se utiliza para almacenar y hacer referencia a otros valores.

### Nombrando una variable
Para nombrar una variable de manera correcta se debe hacer de derecha a izquierda, su operador para asignar una variable es "=". 
```python
variable=100
```
Incorrecta
```python
100=variable
```
No se puede nombrar una variable comenzando por un numero.

```python
1variable=100
```

### Asignando valores a una variable
Las variables se puede asignar numeros y letras sin espacio.

```python
dia=martes
```
Tambien se pueden asignar multiples variables, no es recomendable declarar variable usando la "ñ".
```python
dia=martes
mes=8
anho=2021
```
Se puede declarar variables en una misma linea usando ";".
```python
x = 12; y =10; z=4
```
## Print
Puede imprimir en pantalla varias expresiones separadas por comas o a través de las cadenas, se expresa de la siguiente forma:
```python
print("Hola mundo")
```
se usa el print como funcion, los parensetis y las comillas para el texto a imprimir.
## Introducion por teclado
Para introducir datos por medio de la consola se usa la siguiente linea:
```python
variable=int(input("dato a ingresar:"))
```
Se usa una variable, el int como tipo de dato, el input se usa para digitar un dato a traves de la consola,los parensetis y las comillas para el texto a imprimir.
## Operadores básicos
### Suma
El operador para la suma es "+".
```python
suma=21+8
print(suma)
[output]29
```
Se puede sumar con dos variables.
```python
num1=6
num2=20
suma=num1+num2
print(suma)
[output]26
```
Se puede introducir un numero por medio de la consola.
```python
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
suma=num1+num2
print(num1,'+',num2,'=',suma)
```

### Resta
El operador para la resta es "-".
```python
resta=21-8
print(resta)
[output]13
```
Tambien se puede restar con dos variables.
```python
num1=26
num2=20
resta=num1-num2
print(resta)
[output]6
```
Se puede introducir un numero por medio de la consola.
```python
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
resta=num1-num2
print(num1,'-',num2,'=',resta)
```
### Multiplicación
El operador para la multiplicacion es "*".
```python
multiplicacion=21*8
print(multiplicacion)
[output]168
```
Se puede multiplicar con dos variables.
```python
num1=6
num2=20
multiplicar=num1*num2
print(multiplicar)
[output]|120
```
Se puede introducir un numero por medio de la consola.
```python
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
multiplicacion=num1*num2
print(num1,'*',num2,'=',multiplicacion)
```
### División
El operador para la division es "/".
```python
division=30/2
print(division)
[output]15
```
Se puede dividir con dos variables
```python
num1=30
num2=2
suma=num1/num2
print(division)
[output]15
```
Se puede introducir un numero por medio de la consola.
```python
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
division=num1/num2
print(num1,'/',num2,'=',division)
```
### Módulo
El operador para el modulo es "%"
```python
modulo=21%8
print(modulo)
[output]5
```
Se puede modular con dos variables
```python
num1=6
num2=20
modulo=num1%num2
print(modulo)
[output]6
```
Se puede introducir un numero por medio de la consola.
```python
num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
modulo=num1%num2
print(num1,"%",num2,'=',modulo)
```
## Tipos de datos en Python

### Integer
Este tipo de de datos se corresponde con números enteros, es decir, sin parte decimal, se usa el dato "int" para representarlo.
```python
x = 9
y = 64521
z = -254
```

### Float
Este tipo de dato corresponde con números reales con partes parte decimal. Cabe destacar que el separador decimal en Python es el punto "." y no la coma ",",se usa el dato "float" para representarlo.
```python
x = 9.5
y = 64521.3
z = -254.6
```
### String
Este tipo de datos corresponde con una cadena de caracteres,se usa el dato "str" para representarlo.
```python
cadena=programa de python
variable=hola

```
## Casting en Python
Cast significa convertir un tipo de datos a otro. como int, string o float visto anteriormente, es posible convertir de un tipo a otro.
```python
 int a str: str(46)
 str a int: int ("1245")
 float a int: int (5.14)
```

### List
Son conjuntos ordenados de elementos, los valores de diferentes tipos de datos básicos se pueden agrupar y los elementos se pueden agregar, eliminar o cambiar de las listas en cualquier momento es decir mutables, se representan con corchetes"[]", comillas "" y comas ",".
```python
lista=["mesa", "silla", "ventana"]
 
    print:("lista")
[output]mesa,silla,ventana
```
### Tuple
La tuple es lo mismo que list pero con la diferencia que no se puede reemplazar los datos ingresados es decir inmutables, se representan con corchetes"[]", comillas "" y comas ",".
```python
tuple=[mesa,silla,ventana]
    print:("tuple")
```
### Dictionary

## Tomando decisiones

### Sentencia if,elif y else

### Ciclo For

### Ciclo While

### Break

### Continue
