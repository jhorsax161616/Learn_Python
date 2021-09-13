def binary(objetivo):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def aprox(objetivo):
    paso = epsilon ** 2 
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta ** 2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')


def run():
    objetivo = int(input('Ingresa un numero entero para calcular su raíz cuadrada: '))
    opcion = input('\nIngresa 1 si quiere ralizar busqueda binaria, o 2 si quiere hacer una busqueda por aproximación:\n')
    if opcion == '1':
        binary(objetivo)
    elif opcion == '2':
        aprox(objetivo)
    else:
        print('\n opción inválida ########### \n')
        run()

if __name__ == "__main__":
    print('Calculando la raíz cuadrada de tu número\n')
    epsilon = 0.01
    run()