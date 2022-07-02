#!/usr/bin/env python3
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
def add():
    x = int(input("\u001b[35;1mEnter first number: "))
    y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
    z = x + y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def sub():
    x = int(input("\u001b[35;1mEnter first number: "))
    y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
    z = x - y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def multiply():
    x = int(input("\u001b[35;1mEnter first number: "))
    y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
    z = x * y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def division():
    x = int(input("\u001b[35;1mEnter first number: "))
    y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
    z = x / y
    z = str(z)
    print("\u001b[32;1mThe result is: " +  z)

def mod():
    x = int(input("\u001b[35;1mEnter first number: "))
    y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
    z = x % y
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def percent():
    x = int(input("\u001b[35;1mEnter first number: "))
    y = int(input("\u001b[34;1mEnter second number:  "+"\u001b[0m"))
    z = x * y /100
    z = str(z)
    print("\u001b[32;1mThe result is: " + z)

def power():
    x = int(input("\u001b[35;1mEnter base: "))
    y = int(input("\u001b[34;1mEnter exponent:  "+"\u001b[0m"))
    z = pow(x,y)
    if z != int(z):
        print("\u001b[32;1mThe result is: " + str(z))
    else:
        z = int(z)
        print("\u001b[32;1mThe result is: " + str(z))
    
def sqroot():
    x = int(input("\u001b[35;1mEnter number: \u001b[0m"))
    z = sqrt(x)
    if z != int(z):
        print("\u001b[32;1mThe result is: " + str(z))
    else:
        z = int(z)
        print("\u001b[32;1mThe result is: " + str(z))
    
def h():
    print("\u001b[31;1mAddition: + : For adding two values.")
    print("\u001b[32;1mSubtraction: - : For subtracting two values.")
    print("\u001b[33;1mMultiplication: * : For multiplying two values.")
    print("\u001b[34;1mDivision: / : For dividing two values.")
    print("\u001b[35;1mModulus: _ : For finding the Remainder/Modulus of a value.")
    print("\u001b[36;1mPercentage: % : For finding percentage of a value.")
    print("\u001b[37;1mPower: ^ : For finding the Exponent of values.")
    print("\u001b[31mSquare Root: !  : For finding square root of a single value.")
    print("\u001b[32;1mHelp: h : Shows this page.")
    print("\u001b[33;1mClear Screen: c : To clear the screen")

def c():
    system("cls||clear")

def display():
    print("\u001b[61;1mEnter your operator as follows: \u001b[0m")
    print("\u001b[31;1mAddition: +")
    print("\u001b[32;1mSubtraction: -")
    print("\u001b[33;1mMultiplication: *")
    print("\u001b[34;1mDivision: /")
    print("\u001b[35;1mModulus: _")
    print("\u001b[36;1mPercentage: %")
    print("\u001b[37;1mPower: ^")
    print("\u001b[31mSquare Root: !")
    print("\u001b[32;1mHelp: h")
    print("\u001b[33;1mClear Screen: c")

def main():
    display()
    opt = str(input("\u001b[32;1m> \u001b[0m")).lower()
    if opt == "+":
        add()
    elif opt == "-":
        sub()
    elif opt == "*":
        multiply()
    elif opt == "/":
        division()
    elif opt == "_":
        mod()
    elif opt == "%":
        percent()
    elif opt == "^":
        power()
    elif opt == "!":
        sqroot()
    elif opt == "c":
        c()
        sleep(1)
    elif opt == "h":
        h()
        sleep(0.7)
    else:
        print("\u001b[31mInvalid Operator passed. \u001b[31;1mPlease try again. (Note: Using spaces before or after the operator may trigger this.) \u001b[0m")
        sleep(0.7)
    
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
