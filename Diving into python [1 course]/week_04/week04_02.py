class Value:
    def __set__(self, instance, value):
        self.money = value

    def __get__(self, instance, owner):
        return self.money - (self.money * instance.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
