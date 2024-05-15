import math
print("Welcome to the online banking application")
def signin():
    global name # username
    global pin # password
    global cb #current balance
    name = str(input("Please create your username"))
    pin = str(input("Please create your 6 digiti pin"))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be 6 digits")
        newpin = str(input("Please create your 6 digit pin"))
        if len(newpin) != 6:
            print("The pin has to be 6 digit")
            signin()
        else:
            pin = newpin
    print("Thanks for creating your bank account")
    
def forgotpin():
    recoverpin = str(input("Please create your new 6 digit pin"))
    if len(recoverpin) != 6:
        print("The pin has to be in 6 digits")
        forgotpin()
    else:
        print("The new pin has been stored, please log in")
        pin = recoverpin