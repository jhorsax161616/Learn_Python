def divisors(num):
    assert num > 0, "No se acepta el 0 o números negativos"
    divisors = [i for i in range(1, num +1) if num % i == 0]
    return divisors

def run():
    negative = 1
    num = input("Ingresa un número: ")

    if num[0] == "-":
        num = num[1:]
        negative = -1

    assert num.isdigit(), "Debes ingresar un número"
    print(divisors(int(num) * negative))
    print("Se terminó")

if __name__=='__main__':
    run()