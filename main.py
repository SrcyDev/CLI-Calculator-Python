from math import pow,sqrt
from os import system
from time import sleep
system("")
print('''
    \u001b[33m░█████╗░██╗░░░░░██╗  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
    ██╔══██╗██║░░░░░██║  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░╚═╝██║░░░░░██║  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
    ██║░░██╗██║░░░░░██║  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
    ╚█████╔╝███████╗██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚════╝░╚══════╝╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\u001b[0m
        # Made by \u001b[37;1mSrcyDev\u001b[0m (https://github.com/SrcyDev/)
	    # Project: \u001b[37;1mCLI Calculator Python \u001b[0m (https://github.com/SrcyDev/CLI-Calculator-Python/)
''')
def add(x, y):
    z= x + y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def sub(x, y):
    z = x - y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def multiply(x,y):
    z = x * y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def division(x,y):
    z = x / y
    z = str(z)
    print("\u001b[32;1mThe result is: " +  z)

def mod(x,y):
    z = x % y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def percent(x,y):
    z = x * y /100
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def power(x,y):
    z = pow(x,y)
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def sqroot(x):
    z = sqrt(x)
    print("\u001b[32;1mThe result is: " + str(z))

def main():
    print("\u001b[61;1mEnter your operator as follows: \u001b[0m")
    print("\u001b[31;1mAddition: +")
    print("\u001b[32;1mSubtraction: -")
    print("\u001b[33;1mMultiplication: *")
    print("\u001b[34;1mDivision: /")
    print("\u001b[35;1mModulus: \/")
    print("\u001b[36;1mPercentage: %")
    print("\u001b[37;1mPower: ^")
    print("\u001b[31mSquare Root: !")
    print("\u001b[32;1mHelp: h")
    print("\u001b[33;1mClear Screen: c")
    opt = str(input("\u001b[32;1m> \u001b[0m")).lower()
    if opt == "+":
        x = int(input("\u001b[35;1mEnter first number: "))
        y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
        add(x,y)
    elif opt == "-":
        x = int(input("\u001b[35;1mEnter first number: "))
        y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
        sub(x,y)
    elif opt == "*":
        x = int(input("\u001b[35;1mEnter first number: "))
        y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
        multiply(x,y)
    elif opt == "/":
        x = int(input("\u001b[35;1mEnter first number: "))
        y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
        division(x,y)
    elif opt == "\/":
        x = int(input("\u001b[35;1mEnter first number: "))
        y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
        mod(x,y)
    elif opt == "%":
        x = int(input("\u001b[35;1mEnter first number: "))
        y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
        percent(x,y)
    elif opt == "^":
        x = int(input("\u001b[35;1mEnter first number: "))
        y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
        power(x,y)
    elif opt == "!":
        x = int(input("\u001b[35;1mEnter number: \u001b[0m"))
        sqroot(x)
    elif opt == "c":
        system("cls||clear")
        sleep(1)
    elif opt == "h":
        print("\u001b[31;1mAddition: + : For adding two values.")
        print("\u001b[32;1mSubtraction: - : For subtracting two values.")
        print("\u001b[33;1mMultiplication: * : For multiplying two values.")
        print("\u001b[34;1mDivision: / : For dividing two values.")
        print("\u001b[35;1mModulus: \/ : For finding the remainder of a value.")
        print("\u001b[36;1mPercentage: % : For finding percentage of two values.")
        print("\u001b[37;1mPower: ^ : For finding the Exponent of value.")
        print("\u001b[31mSquare Root: !  : For finding square root of a single value.")
        print("\u001b[32;1mHelp: h : Shows this page.")
        print("\u001b[33;1mClear Screen: c : To clear the screen")
    else:
        print("\u001b[31mInvalid Operator passed. \u001b[31;1mPlease try again. (Note: Using spaces before or after the operator may trigger this.) \u001b[0m")

    
def asked():
    print("\u001b[36mDo you want to continue ([Y]es/[N]o) ?: ")
    ask = str(input("\u001b[32m> \u001b[0m")).lower()
    if ask == "yes" or ask == "ye" or ask == "y" or ask == "":
        main()
        asked()
    elif ask == "no" or ask == "n":
        print("\u001b[31;1mExiting...\u001b[0m")
        quit()
    else:
        print("\u001b[31;1mERRORR.... Please try again\u001b[0m")
        asked()
try:
    main()
    asked()
except KeyboardInterrupt:
    print("\n\u001b[32;1m^C\u001b[0m")
except ValueError:
    print("\u001b[31mInvalid Value(s) passed. \u001b[31;1mPlease try again. (Note: Using spaces before or after values may trigger this.) \u001b[0m")
    main()
    asked()