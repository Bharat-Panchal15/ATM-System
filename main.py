import os
import json
import re

class Account:
    def __init__(self,name,acc_no,pin,balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_pin = pin
        self.balance = balance
    
    @staticmethod
    def from_dict(acc):
        return Account(acc.get('name','Unknown'),acc.get('acc_no','N.A.'),acc.get('acc_pin','N.A.'),acc.get('balance',0))
    
    @staticmethod
    def prompt_acc_no(action=''):
        acc_no = input(f"Enter 6-digit account number {action}: ")
        pattern = re.compile(r"^\d{6}$")

        if not acc_no.isdigit():
            print("Invalid Input! Please enter valid account number.")
            return None
        
        if not re.fullmatch(pattern,acc_no):
            print("Account number must contain 6 digits.")
            return None
        return int(acc_no)
    
    @staticmethod
    def prompt_pin(action=''):
        acc_pin = input(f"Enter 4-digit account pin {action}: ")
        pattern = re.compile(r"^\d{4}$")

        if not acc_pin.isdigit():
            print("Invalid Input! Please enter valid account pin.")
            return None
        
        if not re.fullmatch(pattern,acc_pin):
            print("Account pin must contain 4 digits.")
            return None
        return acc_pin
    
    @staticmethod
    def prompt_amount(action=''):
        amount = input(f"Enter amount {action}:")
        if not amount.isdigit():
            print("Invalid input! amount must contain digits only.")
            return None
        return int(amount)
    
    def to_dict(self):
        return {
            'name':self.name,
            'acc_no':self.acc_no,
            'acc_pin':self.acc_pin,
            'balance':self.balance
            }
    
    def view_balance(self):
        print(f"\nAccount Balance for {self.name} is {self.balance}\n")
    
    def deposit(self,amount):
        if amount is None:
            return
        
        if amount < 2000:
            print("You need to deposit atleast Rs.2000 on each transaction.\n")
            return
        
        self.balance += amount
        print(f"\nRs.{amount} deposited successfully into {self.name}'s account.\n")
    
    def withdraw(self,amount):
        if amount is None:
            return
        
        if amount < 3000 :
            print("You need to withdraw atleast Rs.3000 on each transaction.\n")
            return
        
        elif amount > (self.balance -  2500):
            print("Insufficient Balance. You need atleast Rs.2500 in account for security.")
            return
        
        self.balance -= amount
        print(f"\nRs.{amount} withdrawn successfully from {self.name}'s account.\n")
    
    def change_pin(self):
        old_pin = Account.prompt_pin('to confirm')
        if self.acc_pin != old_pin:
            print("Wrong pin please try again.")
            return

        print("Please enter new pin to update.")
        new_pin = Account.prompt_pin('to update')
        self.acc_pin = new_pin
        print(f"Pin change successfully to {new_pin}")

class ATMsystem:
    def __init__(self,filename='accounts.json'):
        self.accounts = []
        self.filename = filename
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename,'r') as file:
                    data = json.load(file)
                    self.accounts = [Account.from_dict(acc) for acc in data]

            except json.JSONDecodeError:
                print("Error: Corrupt File.Starting fresh.\n")
                self.accounts = []
        
        else:
            self.accounts = []
    
    def save_data(self):
        try:
            with open(self.filename,'w') as file:
                data = [acc.to_dict() for acc in self.accounts]
                json.dump(data,file,indent=4)

        except Exception as e:
            print(f"Error: {e}")
    
    @staticmethod
    def require_login(current_user,action_desc="perform this action"):
        if not current_user:
            print(f"Please login to {action_desc}")
            return False
        return True
    
    def create_acc(self,name,acc_no,pin,balance):
        new_acc = Account(name,acc_no,pin,balance)
        self.accounts.append(new_acc)
        self.save_data()
        print(f"\n✅ Account created successfully for {name}\n")
    
    def login(self,acc_no,pin):
        for acc in self.accounts:
            if acc.acc_no == acc_no and acc.acc_pin == pin:
                print(f"\nLogin Successful. Welcome back {acc.name}\n")
                return acc
            
        print("\nLogin failed\n")
        return None
    
    def logout(self):
        """Always return None to make current_user as None"""
        print("Logout Successful. Thanks for visiting our bank.")
        return None
            
if __name__ == "__main__":
    my_acc = ATMsystem()
    current_user = None

    while True:
        print("\n[1] Register new account")
        print("[2] Login your account")
        print("[3] View Balance")
        print("[4] Deposit amount in account")
        print("[5] Withdraw amount from account")
        print("[6] Change pin of account")
        print("[7] Logout from current account")
        print("[8] Exit from current session\n")

        try:
            user_choice = int(input("Enter your choice: "))

            match user_choice:
                case 1:
                    user_name = input("Enter your name: ")
                    user_acc_no = Account.prompt_acc_no('to register account')
                    for acc in my_acc.accounts:
                        if acc.acc_no == user_acc_no:
                            print("\nAccount already exists!\n")
                            break
                    else:
                        user_pin = Account.prompt_pin('to register account')
                        user_balance = Account.prompt_amount('to deposit initial')

                        if user_balance < 2500:
                            print("\nRegistration Failed!")
                            print("Security deposit while creating account is Rs.2500\n")
                        
                        else:
                            my_acc.create_acc(user_name,user_acc_no,user_pin,user_balance)

                case 2:
                    user_acc_no = Account.prompt_acc_no('to login')
                    user_pin = Account.prompt_pin('to login')
                    current_user = my_acc.login(user_acc_no,user_pin)

                case 3:
                    if ATMsystem.require_login(current_user,"check accout balance.\n"):
                        current_user.view_balance()
                    
                case 4:
                    if ATMsystem.require_login(current_user,"deposit money in your account.\n"):
                        amount = Account.prompt_amount('to deposit')
                        current_user.deposit(amount)
                        my_acc.save_data()

                case 5:
                    if ATMsystem.require_login(current_user,"withdraw money from your account.\n"):
                        amount = Account.prompt_amount('to withdraw')
                        current_user.withdraw(amount)
                        my_acc.save_data()

                case 6:
                    if ATMsystem.require_login(current_user,"change PIN.\n"):
                        current_user.change_pin()
                        my_acc.save_data()

                case 7:
                    if ATMsystem.require_login(current_user,"to logout your account.\n"):
                        current_user = my_acc.logout()

                case 8:
                    print("\nThank you for using ATM System. Goodbye!\n")
                    break

                case _:
                    print("Please enter valid choice!")
        
        except ValueError:
            print("Error: Invalid Input! Please enter a valid input.")