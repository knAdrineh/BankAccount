


class Account():
    def __init__(self, owner="John Wayne", balance=0):
        self.owner = owner
        self.balance = balance

    def __one_hundered_remainder__(self,amount):
        amount = int(amount)
        print(f"Money dispensed:\n100's: ${100 * (amount // 100)}")
        amount = amount % 100
        print(f"20's: {20 * (amount // 20)}")
        amount = amount % 20
        print(f"5's: {5 * (amount // 5)}")
        amount = amount % 5
        print(f"1's: {amount}")

    def __twenties_remainder__(self,amount):
        amount = int(amount)
        print(f"20's: {20 * (amount // 20)}")
        amount = amount % 20
        print(f"5's: {5 * (amount // 5)}")
        amount = amount % 5
        print(f"1's: {amount}")

    def __divisor__(self, amount):
        option = 0
        print("How would you like your cash ?")
        if amount >= 100:
            print("A)100's\nB)20's\n",end="")
            option = input()
            if option.upper() == 'A':
                self.__one_hundered_remainder__(amount)
            elif option == 'B':
                self.__twenties_remainder__(amount)
        elif amount < 100:
            self.__twenties_remainder__(amount)


    def deposit(self, amount=0):
        self.balance += amount
        print(f"${amount:,.2f} deposit complete")

    def withdraw(self, amount):
        while amount > self.balance:
            amount = float(input(f"Enter a valid amount less than {self.balance:,.2f}\n..."))
        self.balance -= amount
        self.__divisor__(amount)
        print(f"${amount:,.2f} withdrawal complete")



    def __str__(self):
        return f"{'-'*15}\nThank you for banking with us {self.owner[0:3]}{'*' * (len(self.owner) - 3)}.\n" \
               f"Current balance: ${self.balance:,.2f}\n{'-'*15}"



