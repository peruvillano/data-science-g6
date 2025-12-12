# RETO 1 :  (JOSÉ VILLANUEVA)
# CREAR UN PROGRAMA USANDO COMO EJEMPLO EL CODIGO DE LA CALCULADORA 
# QUE PERMITA CONVERTIR EL VALOR DE UNA MONEDA DE SOLES A DOLARES Y VICEVERSA,
# POR EJEMPLO SI INGRESO CONVERTIR SOLES A DOLARES E INGRESO 3000 SOLES 
# DEBERIA MOSTRARME SU VALOR EN DOLARES QUE SERIA 1000 DOLARES CONSIDERANDO 
# QUE EL TIPO DE CAMBIO ES 3

# CONVERSOR DE MONEDA
import os
salir = "n"
while(salir == "n"):
    os.system("clear")
    
    print("============= CONVERSOR DE MONEDA ============")
    print("                                              ")
    print("1. De Soles a Dólares")
    print("2. De Dólares a Soles")

    opcion = int(input("Ingrese la opción elegida: "))
    
    if opcion == 1:
        monto = int(input("Ingrese monto en Soles: "))
        tipoc = float(input("Ingrese tipo de cambio: "))
        resultado = float(monto / tipoc)
        print(f" El monto ingresado de S/ {monto} Soles, equivale a US$ {resultado} Dólares")     
        
    elif opcion == 2:
        monto = int(input("Ingrese monto en Dólares: "))
        tipoc = float(input("Ingrese tipo de cambio: "))
        resultado = float(monto * tipoc)
        print(f" El monto ingresado de US$ {monto} Dólares, equivale a S/ {resultado} Soles")
        
    else:
        print("Operación no válida")
        exit()
         
    salir = input("Desea salir? (s/n): ")
    if salir == "s":
        break
    