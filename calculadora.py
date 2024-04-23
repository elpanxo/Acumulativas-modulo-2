# Funciones de la calculadora
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2 

# Menu principal
print("elige una operación:")
print("1. suma")
print("2. resta")
print("3. multiplicación")
print("4. división")

# Solicitar al usuario que ingrese la opción
opcion = input("elige una opcion: 1/2/3/4: ")

# Solicitar al usuario que ingrese los números
num1 = float(input("ingresa el primer número: "))
num2 = float(input("ingresa el segundo número: "))

if opcion == "1": 
    print(num1, "+", num2, "=", suma(num1, num2))

elif opcion == '2':
    print(num1, "-", num2, "=", resta(num1, num2))

elif opcion == '3':
    print(num1, "*", num2, "=", multiplicacion(num1, num2))

elif opcion == '4':
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("Opción inválida")