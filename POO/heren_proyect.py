class Personal:

    def __init__(self, nombre, edad, horas):
        self.nombre = nombre
        self.edad = edad
        self.horas = horas

    def sueldo_mensual(self):
        return self.horas * self.remuneracion * 30

class Gerente(Personal):

    def __init__(self, nombre, edad, horas):
        self.remuneracion = 10
        super().__init__(nombre, edad, horas)

class SubGerente(Personal):

    def __init__(self, nombre, edad, horas):
        self.remuneracion = 7
        super().__init__(nombre, edad, horas)

class Programador(Personal):

    def __init__(self, nombre, edad, horas):
        self.remuneracion = 4
        super().__init__(nombre, edad, horas)

gerente = Gerente('Juan', 34, 8)

subgerente = SubGerente('David', 30, 8)

programador = Programador('Pepe', 19, 12)

print(f'El gerente {gerente.nombre} gana {gerente.sueldo_mensual()}')
print(f'El subgerente {subgerente.nombre} gana {subgerente.sueldo_mensual()}')
print(f'El programador {programador.nombre} gana {programador.sueldo_mensual()}')