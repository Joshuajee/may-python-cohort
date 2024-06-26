class Account:
    name = None
    balance = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def transfer(self, account, amount):
        self.balance -= amount
        account.deposit(amount)
        
    
    
john = Account("John", 1000)
mike = Account("Mike", 500)

def balances():
    print(john.name, john.balance)
    print(mike.name, mike.balance)


balances()

john.deposit(7000)

balances()

john.withdraw(5000)

balances()

mike.withdraw(3000)

balances()

john.transfer(mike, 2800)

balances()

john.balance = 0

balances()