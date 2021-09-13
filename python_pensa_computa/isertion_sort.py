def bubble_sort(lista):
    cont = 0
    for i in range(1, len(lista)):

        for j in range(i):
            cont += 1
            if lista[j] > lista[i]:
                lista[j], lista[i] = lista[i], lista[j]
    print(cont)
    return lista


def ordenamiento_por_insercion(lista):
    cont = 0
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            cont += 1
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    print(cont)
    return lista


if __name__ == '__main__':
    lista = [3, 6, 1, 2, 9, 10, 7,19,23,11,15,8]

    ordenando = ordenamiento_por_insercion(lista)
    print(ordenando)
    ordenan = bubble_sort(lista)
    print(ordenan)