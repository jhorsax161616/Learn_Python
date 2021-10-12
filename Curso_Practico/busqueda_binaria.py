from random import randint
from warnings import resetwarnings

def binary(data, num):
    max = len(data) -1
    min = 0

    while max >= min:
        mid = int((max + min)/2)
        if (num == data[mid]):
            return True
        elif (num < data[mid]):
            max = mid -1
        else:
            min = mid +1
    return False

if __name__=='__main__':
    data =[randint(0,100) for i in range(10)]

    print(f"\n{data}")
    num = int(input('Qué número quieres buscar? '))
    data.sort()
    busq = binary(data, num)

    print(busq)