from random import randint

def burbble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


if __name__ == '__main__':
    size_list = int(input('What size will your list be?: '))

    lis = [randint(0, 100) for i in range(size_list)]
    print(lis)

    ordered_list = burbble_sort(lis)
    print()
    print(ordered_list)