from account import Account

class Car:
    id = int
    license = str
    driver = Account("","")
    passegenger = int

    def __init__(self, licens, drive):
        self.license = licens
        self.driver = drive