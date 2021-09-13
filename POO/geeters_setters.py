class Millas:

    def __init__(self, _distancia = 0):
        self.__distancia = _distancia
    def kilometros(self):
        return (self.__distancia * 2)
    
    @property
    def distancia(self):
        print('obteniendo.....')
        return self.__distancia
    @distancia.setter
    def distancia(self, valor):
        print('definiendo..........')
        if valor < 0:
            raise ValueError('No es posible avansar distancias negativas')
        self.__distancia = valor
    @distancia.deleter
    def distancia(self):
        print('eliminando..................')
        del self.__distancia

    #distancia = property(obtener, definir, eliminar_distancia)


avion = Millas()

avion.distancia = 10

print(avion.distancia)
print(avion.kilometros())
print(avion._Millas__distancia)
del avion.distancia
#print(avion.distancia)
print(avion)
avion.distancia = -10


"""class Human:
    def __init__(self, _temperature = 0):
        self._temperature = _temperature

    @property
    def temperature(self):
        print('obteniendo..........')
        return self._temperature
    @temperature.setter
    def temperature(self, temperature):
        print('validando.............')
        if temperature > 35:
            raise ValueError('Temperatura excedida')
        self._temperature = temperature

    @temperature.deleter
    def temperature(self):
        print('borrando.........')
        del self._temperature


if __name__ == '__main__':
    Ana = Human()
    Ana.temperature = 50
    print(Ana.temperature)"""