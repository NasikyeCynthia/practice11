initial = 300000
transaction1 = input("Hello, which transaction would you like?: ")
transaction = ["withdraw" , "deposit"]
def validation():
    if transaction1 not in transaction:
        print("That transaction is invalid, please try again.")
    elif transaction1 in transaction:
        print("let's proceed")

validation()

import re
amount = float(input("enter amount: "))
m = True
while m:
    if amount > 0:
        break
    elif not re.search("![a-z]",amount):
        break
    elif not re.search("![A-Z]", amount):
        break
    elif not re.search("[0-9]", amount):
        break
    elif not re.search("![$%&]", amount):
        break
    print("Let's proceed!")
    m = False
    break
while m:
    if amount < 0:
        print("The amount is negative")
        break  
    elif not re.search("[a-z]",amount ):
        print("There are letters in your amount")
        break
    elif not re.search("[A-Z]", amount):
        print("There are letters in your amount")
        break
    elif not re.search("![0-9]", amount):
        print("There is no numbers in your amount")
        break
    elif not re.search("[$%&]", amount):
        print("There are symbols in your amount")
        break
