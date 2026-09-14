import json
import random
import string
from pathlib import Path
 

class Bank:
    database = 'data.json'

    data = []

    try:
        if Path(database).exists():
            with open('data.json') as fs:
                data = json.loads(fs.read())
        else: print("no such directory exist")


    except Exception as err:
        print(f"an exception occur as {err}")

    @staticmethod
    def __accountGenerator():
        ch = random.choices(string.ascii_uppercase,k =3)
        num = random.choices(string.digits,k =4)

        accountNumber = ch+num
        return "".join(accountNumber)

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))


    def createAccount(self):
        info ={
            "name" : input("PLease Enter Your Name: "),
            "Age" : int(input("Enter your age: ")),
            "email" : input("Enter your email: "),
            "mobile" : input("enter your mobile no. : "),
            "pin" : input("Create Your account pin: "),
            "accountNumber" : Bank.__accountGenerator() ,
            "balance" : 0,

        }

        if(info["Age"]<18): print("You cannot create an account as your are a minor!")
        else:
            
            while len(info["pin"])!= 4 or not info["pin"].isdigit():
                
                print("Your pin should be of 4 digit!")
                info["pin"] = input("Enter Your account pin: ")
                
            Bank.data.append(info)
            Bank.__update()
            print("\n\nYour account has been created successfully!\n")
            for i in info:
                print(f"    {i} : {info[i]}")
            print("\nPLEASE NOTE YOUR ACCOUNT NUMBER.\n")

    def checkUser(self):
        self.acc = input("Enter your account number: ")
        self.passd = input("Enter Your pin: ")
        
        self.userdata = [i for i in Bank.data if i['accountNumber'] == self.acc and i['pin']==self.passd]

    

    def deposit(self):
        self.checkUser()

        userdata = self.userdata
        

        if(userdata == []): print("Either your account number or pin is invalid")
        else:
            depo = int(input("Enter the amount of deposit: "))
            if(depo<0):
               print("Negative amount cannot deposit")
            else:
                userdata[0]['balance'] += depo

                Bank.__update()

                print("Your Amount has been deposited successfully!")
                print(f"Your Current Balance is {userdata[0]['balance']}")
           

    def withdraw(self):
        self.checkUser()
        
        userdata = self.userdata

        if(userdata == []): print("NO Account found with this information")
        else:
            withMoney = int(input("Enter the ammount of money to withdraw: "))
            if(withMoney<=0):
                print("Withdral money should be greater than 0")
            else:
                if(withMoney > userdata[0]['balance']):
                    print("You cannot withdrawal amount is greator than your balance")
                else:
                    userdata[0]['balance'] -= withMoney

                    Bank.__update()

                    print("Your money has been succeessfully withdraw")
                    print(f"Your current balance is {userdata[0]['balance']}")

    def details(self):
        self.checkUser()
        
        userdata = self.userdata

        if(userdata == []): print("NO Account found with this information")
        else:
            print(f"Your account details for account number {userdata[0]['accountNumber']}")
            for i in userdata[0]:
                print(f"    {i} : {userdata[0][i]}")

    def checkBalance(self):
        self.checkUser()
        
        userdata = self.userdata
        if(userdata == []): print("NO Account found with this information")
        else:
            print(f"Your current account balance is {userdata[0]['balance']}")

    def userUpdate(self):
        self.checkUser()
        
        userdata = self.userdata
        if(userdata == []): print("NO Account found with this information")
        else:
            
            for i in userdata[0]:
                if(i == 'accountNumber' or i == 'balance'):
                    pass
                else:
                    print(f"Your current {i} is {userdata[0][i]}")
                    check = input("Want to update this info? (y/n): ")
                    if(check == 'y'):
                        detail = input(f"Enter Your New {i} : ")
                        userdata[0][i] = detail
                        if i == 'Age':
                            detail = int(detail)

                            if detail < 18:
                                print("Age cannot be less than 18")
                                continue
                        if i == 'pin':
                            while len(detail) != 4 or not detail.isdigit():
                                print("PIN should be exactly 4 digits!")
                                detail = input("Enter your new PIN: ")
                        print(f"Your {i} has been updated")
                    if(check == 'n'):
                        pass
            Bank.__update()

    def deleteAccount(self):
        self.checkUser()
        
        userdata = self.userdata
        if(userdata == []): print("NO Account found with this information")
        else:
            check = input("Are you sure you want to delte your account? (y/n): ")
            if(check == 'y'):
                index = Bank.data.index(userdata[0])
                del Bank.data[index]

                Bank.__update()
            else:
                pass


  
user = Bank()



user = Bank()

while True:
    print("\n========== BANK MENU ==========")
    print("Press 1 for Creating your account")
    print("Press 2 to Withdraw money from your account")
    print("Press 3 to Check balance of your account")
    print("Press 4 to Update details of your account")
    print("Press 5 to Delete your account")
    print("Press 6 to Deposit money")
    print("Press 7 for Details of your account")
    print("Press 8 to Exit")

    task = int(input("\nYour response: "))

    if task == 1:
        user.createAccount()

    elif task == 2:
        user.withdraw()

    elif task == 3:
        user.checkBalance()

    elif task == 4:
        user.userUpdate()

    elif task == 5:
        user.deleteAccount()

    elif task == 6:
        user.deposit()

    elif task == 7:
        user.details()

    elif task == 8:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please try again.")