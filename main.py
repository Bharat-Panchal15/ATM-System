class Account:
    def __init__(self,name,acc_no,pin,balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_pin = pin
        self.balance = balance
    
    def view_balance(self):
        print(f"\nAccount Balance for {self.name} is {self.balance}\n")
    
    def deposit(self,amount):
        self.balance += amount
        print(f"\nRs.{amount} deposited successfully into {self.name}'s account.\n")
    
    def withdraw(self,amount):
        self.balance -= amount
        print(f"\nRs.{amount} withdrawn successfully from {self.name}'s account.\n")
    
    def change_pin(self,new_pin):
        self.acc_pin = new_pin
        print(f"Pin change successfully to {new_pin}")

class ATMsystem:
    def __init__(self):
        self.accounts = []
    
    def create_acc(self,name,acc_no,pin,balance):
        new_acc = Account(name,acc_no,pin,balance)
        self.accounts.append(new_acc)
        print(f"\n✅ Account created successfully for {name}\n")
    
    def login(self,acc_no,pin):
        for acc in self.accounts:
            if acc.acc_no == acc_no and acc.acc_pin == pin:
                print(f"\nLogin Successful. Welcome back {acc.name}\n")
                return acc
            
        print("\nLogin failed\n")
    
    def logout(self,acc):
        self.accounts.remove(acc)
        print("Logout Sucessful. Thanks for visiting our bank.")
        return None
            

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

    user_choice = int(input("Enter your choice: "))

    match user_choice:
        case 1:
            user_name = input("Enter your name: ")
            user_acc_no = int(input("Enter account number: "))
            for acc in my_acc.accounts:
                if acc.acc_no == user_acc_no:
                    print("\nAccount already exists!\n")
                    break
            else:
                user_pin = int(input("Enter user pin: "))
                user_balance = int(input("Deposit initial balance: "))

                if user_balance < 2500:
                    print("\nRegistration Failed!")
                    print("Security deposit while creating account is Rs.2500\n")
                
                else:
                    my_acc.create_acc(user_name,user_acc_no,user_pin,user_balance)

        case 2:
            user_acc_no = int(input("Enter account number to login: "))
            user_pin = int(input("Enter your pin: "))

            current_user = my_acc.login(user_acc_no,user_pin)

        case 3:
            if current_user:
                current_user.view_balance()
            
            else:
                print("Please login to check account balance.")
            
        case 4:
            if current_user:
                amount = int(input("Enter how much amount to deposit: "))

                if amount >= 2000:
                    current_user.deposit(amount)
                
                else:
                    print("You need to deposit atleast Rs.2000 on each transaction.\n")    

            else:
                print("Please login to deposit money in your account.\n")
        
        case 5:
            if current_user:
                amount = int(input("Enter how much amount to withdraw: "))

                if amount < 3000 :
                    print("You need to withdraw atleast Rs.3000 on each transaction.\n")
                
                elif amount > (current_user.balance -  2500):
                    print("Insufficient Balance. You need atleast Rs.2500 in account for security.")
                
                else:
                    current_user.withdraw(amount)
            else:
                print("Please login to withdraw money from you account.\n")

        case 6:
            if current_user:
                old_pin = int(input("Enter previous pin to confirm: "))

                if current_user.acc_pin == old_pin:
                    print("Please enter new pin to update.")
                    new_pin = int(input("Enter new pin: "))

                    current_user.change_pin(new_pin)
                
                else:
                    print("Wrong pin please try again.")
            
            else:
                print("Please login to change pin.")

        case 7:
            if current_user:
                current_user = my_acc.logout(current_user)
            
            else:
                print("Logout failed. Please login.")

        case 8:
            print("\nThank you for using ATM System. Goodbye!\n")
            break

        case _:
            print("Please enter valid input!")