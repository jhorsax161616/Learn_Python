class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    
    rectangu1 = Rectangulo(3, 4)
    print(rectangu1.area())

    cuadrado1 = Cuadrado(5)
    
    print(cuadrado1.area())