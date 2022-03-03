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
Tambien se pueden asignar multiples variables, no es recomendable declarar variable usando la "ñ"
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
se usa el print como funcion, los parensetis y las comillas para el texto a imprimir
## Introducion por teclado
Para introducir datos por medio de la consola se usa la siguiente linea:
```python
variable=int(input("dato a ingresar:"))
```
Se usa una variable, el int como tipo de dato, el input se usa para digitar un dato a traves de la consola,los parensetis y las comillas para el texto a imprimir
## Operadores básicos
### Suma
El operador para la suma es "+"
```python
suma=21+8
print(suma)
[output]29
```
Se puede sumar con dos variables
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
sum1=num1+num2
print(num1,'+',num2,'=',sum1)
```

### Resta
El operador para la resta es "-"
```python
resta=21-8
print(resta)
[output]13
```
Tambien se puede restar con dos variables
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

### División

### Módulo

## Tipos de datos en Python

### Integer

### Float

### String

## Casting en Python

### List

### Tuple

### Dictionary

## Tomando decisiones

### Sentencia if,elif y else

### Ciclo For

### Ciclo While

### Break

### Continue
