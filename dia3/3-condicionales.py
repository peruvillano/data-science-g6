# datos de entrada
#numero1 = 10
#numero2 = 5
numero1 = int(input("ingrese el primer número "))
numero2 = int(input("ingrese el segundo número "))
operacion= input("ingrese la operacion a realizar (+ , - , * , /) : ")

# proceso
#suma = numero1 + numero2
if operacion == "+":
    resultado = numero1 + numero2
#else:
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    print("OPERACIÓN NO VÁLIDA!!!")
    exit()

# datos de salida
#print("la suma de los numeros es: ", suma)

print(f"{numero1}{operacion}{numero2}={resultado}")

