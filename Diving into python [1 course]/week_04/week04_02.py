class Value:
    def __init__(self):
        self.money = 0

    def __set__(self, instance, value):
        self.money = value

    def __get__(self, instance, owner):
        return self.money - (self.money * instance.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
