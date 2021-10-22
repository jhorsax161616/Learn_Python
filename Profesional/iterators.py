import time

class FiboIter():

    def __init__(self, max = None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        elif not self.max or self.counter <= self.max - 1:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux #Intercambio
            self.counter += 1
            return self.aux
        else:
            raise StopIteration

if __name__=='__main__':

    print("===Generando Sucesión Fibonacci===")

    lenn = None
    try:
        lenn = int(input("\nIngrese cantidad de números que desee: "))
        if lenn <= 0:
            raise ValueError
    except ValueError:
        lenn = None
        print("Se imprimirá hasta al infinito!!")

    fibonacci = FiboIter(lenn)

    for count, number in enumerate(fibonacci):
        print(f"{count + 1} número: {number}")
        time.sleep(.5)