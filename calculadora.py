Phyton

print("Calculadora Basica")

num1 = float(input("Ingresa el primer numero"))
num2 = float(input("Ingresa el segundo numero"))

print("Selecciona Operacion")
print("1. SUMAR")
print("2. RESTAR")
print("3. MULTIPLICAR")
print("4. DIVIDIR")

op = input("Elige una opcion (1/2/3/4): ")

if op == "1":
print("Resultado:",num1 + num2)

elif op == "2":
print("Resultado:", num1 - num2)

elif op == "3":
print("Resultado:", num1 * num2)

elif op == "4":
print("Resultado:", num1 / num2)

else:
print("Opcion no valida")
