# This is code for assignment 007/1 Python If Statements
login = {"Elnur": "W@12"}
name = input("Please, enter your name: ")
if name == list(login.keys())[0]:
    print(f"Hello, {list(login.keys())[0]}! The password is : {list(login.values())[0]}")
else:
    print(f"Hello, {name}! See you later.")
