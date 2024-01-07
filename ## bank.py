import random

newuser = {
    "name": "azoz",
    "password": "12",
    "accountnotsuspended": True,
    "iban": "1111",
    "balence": 9000
}

newuser1 = {
    "name": "azoz1",
    "password": "123",
    "accountnotsuspended": True,
    "iban": "2222",
    "balence": 1000
}

data = [newuser, newuser1]

def login():
    username = input("hello please enter your username ")
    password = input("enter your password ")

    user_exists = False
    loginsuccess = False
    current_user = None

    for user in data:
        if user["name"] == username:
            user_exists = True
            if user["password"] == password and user["accountnotsuspended"]:
                print("welcome")
                loginsuccess = True
                current_user = user
            elif user["password"] == password and not user["accountnotsuspended"]:
                print("your account is suspended please visit the bank")

    if not user_exists:
        print("User does not exist")

    return loginsuccess, current_user

def operations(loginmade):
    loginsuccess, user = loginmade
    if loginsuccess:
        operation = input("what operation would you like to make \n1-transfer \n2-deposit \n3-withdraw \n")
        if operation == "1":
            destination_iban = input("Enter the iban of the person you would like to transfer to: ")
            destination_user = None
            for otheruser in data:
                if otheruser.get("iban") == destination_iban:
                    destination_user = otheruser
            if not otheruser.get("iban") == destination_iban:
                print("user does not exist")
            amount = float(input("Enter the amount to transfer: "))

            

            if amount <= user["balence"]:
                newbalence = user["balence"] - amount
                print(f"tranfer has beeen completed and {amount} has been reduced from your bank balence your new bank balence is {newbalence}")
                print(f"transferring {amount} to {destination_iban}")
                otheruser["balence"] += amount
            else:
                print("cannot transfer this ammount it is bigger then your balence ")
        elif operation == "2":
            amount = input("enter the amount to deposit in the money tray: ")
            print(f"depositing {amount}")

        elif operation == "3":
            amount = float(input("enter the amount to withdraw: "))
            newbalence = user["balence"] - amount
            print(f"Withdrawing {amount}")

        else:
            print("invalid operation Please choose a valid operation")


loginmade = login()
operations(loginmade)
