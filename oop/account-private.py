class Account:
    name = None
    __balance = 0
    
    def __init__(self, name, __balance):
        self.name = name
        self.__balance = __balance
        
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
        
    def transfer(self, account, amount):
        self.__balance -= amount
        account.deposit(amount)
    
    def getBalance(self):
        return self.__balance
    
    
    
john = Account("John", 1000)
mike = Account("Mike", 500)

def __balances():
    print(john.name, john.getBalance())
    print(mike.name, mike.getBalance())


__balances()

john.deposit(7000)

__balances()

john.withdraw(5000)

__balances()

mike.withdraw(3000)

__balances()

john.transfer(mike, 2800)

__balances()

john.__balance = 10

__balances()