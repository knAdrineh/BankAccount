#Adrineh Khodaverdian
from bank_account import Account


def main():

    acc = Account("Java table",500)
    print(acc)
    acc.deposit(300)
    print(acc)
    amount = float(input("Enter amount to withdraw : "))
    acc.withdraw(amount)
    print(acc)


main()