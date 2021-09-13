class Auto:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca       
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(4,'GAS')

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)
        self._estado = 'en movimiento'
class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.cantidad_gasolina = 0
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        self.cantidad_gasolina += cantidad

if __name__ == '__main__':
    auto1 = Auto('ferrari', 'samsung', 'rojo')
    print(auto1.modelo, auto1.marca, auto1._motor.tipo, auto1._estado)
    print(auto1._motor.cantidad_gasolina)
    auto1._motor.inyecta_gasolina(100)
    print(auto1._motor.cantidad_gasolina)
    auto1.acelerar('rapida')
    print(auto1.modelo, auto1.marca, auto1._motor.tipo, auto1._estado)
    print(auto1._motor.cantidad_gasolina)