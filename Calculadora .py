# Calculadora-Basica
Calculadora Básica
text
def sumar(x, y):
return x + y
def restar(x- y):
return x - y
def multiplicar(x, y):
return x * y
def dividir(x, y):
if y != 0:
return x  / y
return "ERROR: DIVISION POR CERO"
print("Calculadora Simple")
num1 = float(input("Primer número: "))
num2 = float(input(Segundo número: ))
operaciion = input "Operación (+, -, *, /):")
if operacion == '+':
print(sumar(num1, num2))
operaciion = input "Operación (+, -, *, /):")
elif operacion == '-':
print(restar(num1, num2))
operaciion = input "Operación (+, -, *, /):")
elif operacion == '*':
print(multiplicar(num1, num2))
operaciion = input "Operación (+, -, *, /):")
elif operacion == '/':
print(dividir(num1, num2))
else:
print("Operacion Invalida")
