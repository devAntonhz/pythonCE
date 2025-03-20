def suma(*numero):
    resultado = 0
    for num in numero:
        resultado += num
    print(resultado)


suma(20, 10)
suma(20, 10, 40)
suma(20, 10, 50, 50)
suma(20, 10, 90, 90, 90, 90)
