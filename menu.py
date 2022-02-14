from statistics import mean
from tamm import *
m = Math
am = Advancedmath
t = Trigonomitry

def menu3():
    print("{------------------ Page 3 --------------------}")
    print("||||||||||||||||||||||||||||||||||||||||||||||||")
    print("{--1-- Percentage---}||||{-2 Pathagorean triple}")
    print("{--3- Pathagorean unkown var}|||||||||||||||||||")
    menu1 = int(input("Enter: "))
    if menu1 ==1:
        am.percent(int(input("Enter percent: ")), int(input("Enter number: ")))


def menu2():
    print("{-----------------Page 2 -----------------}")
    print("|||||||||||||||||||||||||||||||||||||||||||")
    print("{--1--- Mean -----}||||{--2--- MAD -------}")
    print("{--3 Square Root -}||||{--4--- Power -----}")
    print("{----------------------- 5 -->>>  Page 3 -}")
    menu1 = int(input("Enter: "))
    if menu1 ==1:
        var1 = input('Enter numbers:')
        input1 = list(map(int,var1.split(' ')))
        am.mean(input1)
    elif menu1 ==2:
        var2 = input('Enter numbers:')
        input2 = list(map(int,var2.split(' ')))
        am.mad(input2)
    elif menu1 ==3:
        am.squareroot(int(input("Enter number: ")))
    elif menu1 ==4:
        am.power(int(input("Enter number to power: ", int(input("Enter power number: ")))))
    elif menu1 ==5:
        menu3()





def menu1():
    print("{-----------------Page 1 -----------------}")
    print("|||||||||||||||||||||||||||||||||||||||||||")
    print("{--1--- Add ------}||||{--2--- Subtract --}")
    print("{--3--- Multiply -}||||{--4--- Divide ----}")
    print("{----------------------- 5 -->>>  Page 2 -}")
    menu1 = int(input("Enter: "))
    if menu1 == 1:
        m.add(int(input("Enter first Number: ")), int(input("Enter second Number: ")))
    elif menu1 ==2:
        m.subtract(int(input("Enter first Number: ")), int(input("Enter second Number: ")))    
    elif menu1 ==3:
        m.multiply(int(input("Enter first Number: ")), int(input("Enter second Number: ")))
    elif menu1 ==4:
        m.divide(int(input("Enter first Number: ")), int(input("Enter second Number: ")))
    elif menu1 ==5:
        menu2()    