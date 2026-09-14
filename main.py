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
            "mobile" : int(input("enter your mobile no. : ")),
            "pin" : int(input("Create Your account pin: ")),
            "accountNumber" : Bank.__accountGenerator() ,
            "balance" : 0,

        }

        if info["Age"]<18 or len(info["pin"])!= 4:
            print("sorry you cannot create an account!")
        else:
            Bank.data.append(info)
            Bank.__update()
            print("Your account has been created successfully!\n")
            for i in info:
                print(f"    {i} : {info[i]}")
            print("\nPLEASE NOTE YOUR ACCOUNT NUMBER.\n")

   


    def deposit(self):
        acc = input("Enter your account number: ")
        passd = int(input("Enter Your pin: "))

        userdata = [i for i in Bank.data if i['accountNumber'] == acc and i['pin']==passd]

        if(userdata == False): print("Either your account number or pin is invalid")
        else:
           depo = int(input("Enter the amount of deposit: "))
           userdata[0]['balance'] += depo

           Bank.__update()

           print("Your Amount has been deposited successfully!")
           print(f"Your Current Balance is {userdata[0]['balance']}")

    def withdraw(self):
        acc = input("Please enter your account number: ")
        paasd = input("Please enter your pin: ")

        userdata = [i for i in Bank.data if i['accountNumber']== acc and i['pin'] == paasd]

        if(userdata == False): print("NO Account found with this information")
        else:
            withMoney = int(input("Enter the ammount of money to withdraw: "))
            userdata[0]['balance'] -= withMoney

            Bank.__update

            print("Your money has been succeessfully withdraw")
            print(f"Your current balance is {userdata[0]['balance']}")

    def details(self):
        acc = input("Please enter your account number: ")
        paasd = input("Please enter your pin: ")
        
        userdata = [i for i in Bank.data if i['accountNumber']== acc and i['pin'] == paasd]
        if(userdata == False): print("NO Account found with this information")
        else:
            print(f"Your account details for account number {userdata[0]['accountNumber']}")
            for i in userdata[0]:
                print(f"    {i} : {userdata[0][i]}")

    def checkBalance(self):
        acc = input("Please enter your account number: ")
        paasd = input("Please enter your pin: ")
                
        userdata = [i for i in Bank.data if i['accountNumber']== acc and i['pin'] == paasd]
        if(userdata == False): print("NO Account found with this information")
        else:
            print(f"Your current account balance is {userdata[0]['balance']}")

    def userUpdate(self):
        acc = input("Please enter your account number: ")
        paasd = input("Please enter your pin: ")

        userdata = [i for i in Bank.data if i['accountNumber']== acc and i['pin'] == paasd]
        if(userdata == False): print("NO Account found with this information")
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
                        print(f"Your {i} has been updated")
                    if(check == 'no'):
                        pass
            Bank.__update()

    def deleteAccount(self):
        acc = input("Please enter your account number: ")
        paasd = input("Please enter your pin: ")
        
        userdata = [i for i in Bank.data if i['accountNumber']== acc and i['pin'] == paasd]
        if(userdata == False): print("NO Account found with this information")
        else:
            check = input("Are you sure you want to delte your account? (y/n): ")
            if(check == 'y'):
                index = Bank.data.index(userdata[0])
                del Bank.data[index]

                Bank.__update()
            else:
                pass


  
user = Bank()




print("Press 1 for Creating your account")
print("Press 2 to widthdraw money from  youraccount")
print("Press 3 check balance of your account")
print("Press 4 for Updating details of your account")
print("Press 5 for Delete your account")
print("Press 6 to Deposit money ")
print("Press 7 for details of your account")

task = int(input("Your response: "))

if (task == 1):
    user.createAccount()

if(task ==2):
    user.withdraw()
if(task ==3):
    user.checkBalance()
if(task == 4):
    user.userUpdate()
if(task == 5):
    user.deleteAccount()
if(task == 6):
    user.deposit()
if(task == 7):
    user.details()
