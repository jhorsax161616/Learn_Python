class Hotel:
    

    def __init__(self, num_max, lug_esta):
        #super().__init__()
        self.num_max = num_max
        self.lug_esta = lug_esta
        self.persons = 0

    def anadir(self, cantidad):
        self.persons += cantidad
    def reducir(self, cantidad):
        self.persons -= cantidad
    def numero(self):
        return self.persons

hotel = Hotel(3, 5)
print(hotel.num_max, hotel.lug_esta)
print(hotel.persons)
hotel.anadir(5)
print(hotel.persons)
hotel.reducir(2)
print(hotel.persons)
a = hotel.numero()
print(a)
hotel.anadir(10)
print(hotel.persons)