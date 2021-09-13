class Casilla:
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__regio = None
        self.__secreto = "Rose"

    @property
    def region(self):
            return self.__regio
    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__regio = region
            print('Felicitaciones es aceptado')
        else:
            raise ValueError(f'La region {region} no es aceptada en {self.__pais}')
        

if __name__ == '__main__':
    casi = Casilla(121, ['Huancayo', 'Perú', 'Lima'])
    print(casi.region, casi._Casilla__pais, casi._Casilla__identificador)
    casi.region = 'Lima'
    print(casi._Casilla__regio)