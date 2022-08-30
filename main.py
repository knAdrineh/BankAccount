#Adrineh Khodaverdian
'''
A simple bank account app
'''
from bank_account import Account


if __name__ == '__main__':

    acc = Account("Java table",500)
    print(acc)
    acc.deposit(300)
    print(acc)
    while True:
    try:
        amount = float(input("Enter amount to withdraw : "))
    except:
        print("Invalid input!")
        continue
    else:
        break
    acc.withdraw(amount)
    print(acc)


