class bank:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
    
    # def __repr__(self):
    #     return "hello"

    def deposit(self, amount):
        if amount > 0:
            balance += amount
    
    def withdraw(self, amount):
        if amount < self.balance:
            balance -= amount
            return amount
        else :
            return "not enough money"
    
    def get_balance(self):
        return self.__balance
    
nur = bank("nur", 10000)
# print(nur.__name)
# print(nur.__balance)
print(nur.get_balance())