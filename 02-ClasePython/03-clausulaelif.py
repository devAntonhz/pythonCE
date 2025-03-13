# edad = int(input("Digite su edad: "))

# if edad > 99:
#     print("Edad no reconocida")
# elif edad >= 18:
#     print("Puede ver la pelicula")
# elif edad >= 11:
#     print("Necesita el permiso de los padres")
# elif edad < 0:
#     print("Edad erronea")
# else:
#     print("No puede ver la pelicula")

# ? FORMULA
# ? peso / (altura * altura)
# ! TODO: TAREA: CALCULA EL IMC DE UNA PERSONA:
# HALLAREMOS EL ÍNDICE DE SOBREPESO (IMC):
peso = float(input("peso:"))
altura = float(input("altura:"))
imc = peso / (altura * altura)
if imc < 18.5:
    print("peso insuficiente")
elif imc >= 18.5 and imc < 24.9:
    print("normal")
elif imc >= 25 and imc < 29.9:
    print("sobrepeso")
elif imc >= 30 and imc < 34.9:
    print("obesidad")
elif imc >= 35:
    print("obesidad extrema")
