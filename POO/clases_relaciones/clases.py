from car import Car
from account import Account
from UberX import UberX
from card import Card
from Efectivo import Cash
#from payment import Payment

if __name__ == "__main__":
    """car = Car()
    car.license = "ASFASF"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "QWFQQ"
    car2.driver = "Andrea Herreron"
    print(vars(car2))"""

    """car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))"""

    #car2 = Car("AAAAA", Account("ANDRE", "7771"), UberX())
    car3 = UberX("AAAAA3", Account("ANDREww", "777169"), "Mazda", "Super2020")
    print(vars(car3))
    print(vars(car3.driver))

    pago = Card(13, "Soles", 7156623884, 356, "10/23")
    print(vars(pago))