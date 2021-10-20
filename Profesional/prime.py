from typing import List

def is_prime(number: int) -> bool:
    dividers: List[int] = [i for i in range(1, int(number/2)+1) if number % i == 0]   
    
    if len(dividers) == 1:
        return True
    return False

def run() -> None:
    test: int = int(input("Ingrese un número: "))
    print(is_prime(test))

if __name__ == '__main__':
    run()