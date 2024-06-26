class Account:
    name = None
    __balance = 0
    __pin = None
    
    def __init__(self, name, pin, balance):
        self.name = name
        self.__pin = pin
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, pin, amount):
        if (self._compare_pin(pin)):
            self.__balance -= amount
        
    def transfer(self, pin, account, amount):
        if (self._compare_pin(pin)):
            self.__balance -= amount
            account.deposit(amount)
        else: print("Incorrect Pin")
    
    def getBalance(self):
        return self.__balance
    
    def _compare_pin(self, pin):
        if (self.__pin == pin): return True
        return False
    
    
    
john = Account("John", 0000, 1000)
mike = Account("Mike", 1111, 500)


class CurrentAccount(Account):
    def viewPin(self):
        super().__pin
    def compare_pin(self, pin):
        return super()._compare_pin(pin)


def __balances():
    print(john.name, john.getBalance())
    print(mike.name, mike.getBalance())


__balances()

john.deposit(7000)

__balances()

john.withdraw(0000, 5000)

__balances()

mike.withdraw(0000,3000)

__balances()

john.transfer(mike, 0000, 2800)

__balances()

john.__balance = 10


print(john._compare_pin(0000))
__balances()



boss = CurrentAccount("Boss", 2222, 10000)

## won't work because this method uses the __pin variable which is private
#boss.viewPin()
