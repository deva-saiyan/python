class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f'Account created!\nName: {self.name} \nBalance: {self.balance}\n')

    def show_balance(self):
        print(f'Name: {self.name} \nCurrent Balance: {self.balance}\n')

    def aura(self):
        print('guygu')  # now aura is part of Bank


class Balance(Bank):
    def credit(self):
        amount = int(input('Enter amount to deposit: '))
        self.balance += amount
        print(f'Deposited ₹{amount}')
        self.show_balance()

    def debit(self):
        amount = int(input('Enter amount to withdraw: '))
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawn ₹{amount}')
        else:
            print('Insufficient balance!')
        self.show_balance()

    def asa(self):
        super().show_balance()  # this now works
# Create an object of Bank class
deva = Balance('Deva')

# Call credit method
deva.credit()
deva.asa()