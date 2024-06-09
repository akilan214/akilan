class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  
        self.__balance = initial_balance       

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        else:
            return "Insufficient balance or invalid amount."

    def get_balance(self):
        return f"Current balance: {self.__balance}"

    def get_account_number(self):
        return f"Account number: {self.__account_number}"

account = BankAccount("123456789", 1000)

print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())

try:
    print(account.__balance)
except AttributeError:
    print("Cannot access private variable __balance")

print(account._BankAccount__balance) 
