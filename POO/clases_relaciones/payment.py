class Payment:
    id = int
    amount = int
    kind = str

    def __init__(self, amount, kind):
        self.amount = amount
        self.kind = kind