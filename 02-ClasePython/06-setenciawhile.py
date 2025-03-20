# while "hola" == "hola":
# #     pass

# numero = 10

# while numero > 5:
#     print(numero)

# numero = 10

# while numero > 0:
#     numero -= 1
#     print(numero)

numero = 20

# WHile de una linea
# while numero >= 20: print(numero); numero+= 1

# Menu interactivo cion while

# while True:
#     print("1. Ver Saludo")
#     print("2. Ver Despedida")
#     print("3. Salida")

#     opcion = input("Elige un opcion: ")

#     if opcion == "1":
#         print("Hola amigo \n")
#     elif opcion == "2":
#         print("Chao amigo \n")
#     else:
#         print("Saliendo del programa \n")
#         break

# ? SUMAR NUMERO HASTA EL USUARIO INGRESE EL VALOR DE 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Ingresa un numero (0: Finalizar): "))
    suma += numero

print("La suma total es:", suma)
