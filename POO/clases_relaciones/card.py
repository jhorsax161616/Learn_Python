from payment import Payment

class Card(Payment):
    number = int
    cvv = int
    date = str

    def __init__(self, amount, kind, number, cvv, date):
        super().__init__(amount, kind)
        self.number = number
        self.cvv = cvv
        self.date = date