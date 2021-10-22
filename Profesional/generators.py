import time

def fibo_gen(max: int):
    n1 = 0
    n2 = 1
    counter = 0

    while counter <= max - 1:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__=='__main__':

    lenn = int(input("Ingrese hasta cuantos números de Fibonacci quiere: "))
    fibonacci = fibo_gen(lenn)

    for count, number in enumerate(fibonacci):
        print(f"{count + 1} número: {number}")
        time.sleep(.5)