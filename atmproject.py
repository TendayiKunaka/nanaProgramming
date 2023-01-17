import random
import sys


class ATM:
    def __init__(self, name, surname, account_number, balance=0):
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print("____________ ACCOUNT DETAILS ____________")
        print(f"Account Holder: {self.name} {self.surname}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current Account Balance: $", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds")
            print(f"Your balance is ${self.balance}")
            print(f"Please Try With A Lesser Amount")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"${self.amount} withdrawal successful!")
            print(f"Current Account Balance: {self.balance}")

    def check_balance(self):
        print(f"Available Balance: ${self.balance}")
        print()

    def transaction(self):
        print("""
              TRANSACTION
        *************************
          Menu:
          1. Account Detail
          2. Check Balance
          3. Deposit
          4. Withdrawal
          5. Exit
        *************************
        """)
        while True:
            try:
                option = int(input("Enter option 1 - 5: "))
            except:
                print("Error: Enter option 1-5 only")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("Deposit Amount: $"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("Withdrawal Amount: $"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f""" 
                PRINTING RECEIPT......................
            *********************************************
               Transaction is now complete
               Transaction number: {random.randint(100000, 3999999)}
               Account Holder: {self.name.upper()} {self.surname.upper()}
               Account Number: {self.account_number}
               Available Balance: ${self.balance}
               
               Thank You For Choosing Us, The Bank Of Choice
               Open City, always at your service............
            ***********************************************            
""")
  #          sys.exit()


print("************** Welcome To OpenCit **************")
print("________________________________________________")
print("Account Creation:")
name = input("Enter Your Name: ")
surname = input("Enter Your Surname: ")
account_number = input("Account Number: ")
print("________________________________________________")
print("Congratulations!!!!!!!!!!!!!!!!!!!")
print("Account Created successfully...... \n")
print(f"""
        Name:           {surname} {name}
        Account Number: {account_number}
        Branch:          Online Bank

""")

atm = ATM(name, surname, account_number)
while True:
    trans = input("Do you want to transact? (y/n): ")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
        -------------------------------------
        Thanks for choosing us as your bank 
                  Visit us again!                     
        -------------------------------------
        
        """)
        break
    else:
        print("Wrong Command")
