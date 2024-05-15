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
        
        
def depositinterest(p,r,t):
    # A = Pe^(rt) which is the formula for calculating the compound interest
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    #Calculation
    a =  p * e #Future value of your investment
    return a

def login():
    # name1 represent username
    # pin1 represent user's pin
    name1 = str(input("Please enter your username"))
    pin1 = str(input("Please enter your pin"))
    # Check if the name and pin matched
    if name1 == name and pin1 == pin:
        print("Welcome to the online banking application" + " " + name)
        print("Please choose the menu down here")
        listmenu = ["1-Deposit","2-Withdraw","3-Transfer","4-Check","5-Deposit interest rate","6-Calculate compound interest"]
        for b in listmenu:
            print(b)
        choose = int(input("Please enter the number of your chose"))
        d = 0
        w = 0
        cb = 0
    
    
    
    else:
       print("Either of your username or pin is wrong, did you create your account")
       list1 = ["1-yes","2-no"]
       for i in list1:
           print(i)
    inp = int(input("Enter your choice below"))
    if inp == 1:
        list2 = ["1-do you want to attempt to log in again?", "2-You forgot your pin?"]
        for e in list2:
            print(e)
        theanswer = str(input("Please enter your choice"))
        theanswer = int(theanswer)
        if theanswer == 1:
            login()
        elif theanswer == 2:
            forgotpin()
        else:
            print("Option is not available")
            login()
    elif inp == 2:
        print("Please create your account")
        signin()