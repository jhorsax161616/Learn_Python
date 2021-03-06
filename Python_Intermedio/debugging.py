def divisors(num):
    try:
        if num <= 0:
            raise ValueError("Debes ingresar un número positivo")
        divisors = [i for i in range(1, num +1) if num % i == 0]
        return divisors
    except ValueError as ve:
        return ve

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Se terminó")
    except ValueError:
        print("Ingresa un número ")

if __name__=='__main__':
    run()