
print("Antes:")
numeros = [1,2,3,2,2,5,6,7,7,8,8,2,3,2,2,1,3,4,5,6]
print(numeros)

#El tipo de dato set es similar a una lista pero este no guarda datos repetidos
print()
print("Con set_")
no_repetidos = {num for num in numeros}

print(no_repetidos)