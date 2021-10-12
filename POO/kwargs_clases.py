class Punto:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    #Sirve para hacer un print directo con el objeto
    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

class Circulo(Punto):
    def __init__(self, radio, *args, **kwargs) -> None:
        self.radio = radio
        super().__init__(*args, **kwargs)
    
    def __repr__(self) -> str:
        return super().__repr__() + f", radio: {self.radio}"


print(Circulo(100, 4, 2))

cdr1 = Circulo(12, 5, 5)
cdr2 = Circulo(10, -5, 5)

print(cdr1)