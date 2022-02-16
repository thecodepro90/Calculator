from tamm import *
m = Math
am = Advancedmath
t = Trigonomitry

def gobacktomenu(a):
    if a ==1:
        from menu import menu1
        menu1()
    elif a ==2:
        from menu import menu2
        menu2()
    elif a ==2:
        from menu import menu3
        menu3()

def menu3():
    print("{------------------ Page 3 --------------------}")
    print("||||||||||||||||||||||||||||||||||||||||||||||||")
    print("{--1-- Percentage---}||||{-2 Pathagorean triple}")
    print("{--3- Pathagorean unkown var}|||||||||||||||||||")
    print("{---<<< Page 2 << 5 ---------------------------}")
    menuenter = input("Enter: ")
    if menuenter =="1":
        am.percent(int(input("Enter percent: ")), int(input("Enter number: ")))
        gobacktomenu(3)
    elif menuenter =="2":
        t.pathagoreantriple(int(input("Enter first side")), int(input("Enter second side")), int(input("Enter third side")))
        gobacktomenu(3)
    elif menuenter =="3":
        t.pathagoreanunkownvar(int(input("Enter leg 1: ")), int(input("Enter leg 2: ")), input("Enter unkown side: "))
        gobacktomenu(3)
    elif menuenter =="devmode":
        from devmenu import devmenu1, devmode
        devmode()
    elif menuenter =="5":
        gobacktomenu(2)
    else:
        gobacktomenu(3)

def menu2():
    print("{-----------------Page 2 -----------------}")
    print("|||||||||||||||||||||||||||||||||||||||||||")
    print("{--1--- Mean -----}||||{--2--- MAD -------}")
    print("{--3 Square Root -}||||{--4--- Power -----}")
    print("{- Page 1 <<<-- 5 ------ 6 -->>>  Page 3 -}")
    menuenter = int(input("Enter: "))
    if menuenter ==1:
        var1 = input('Enter numbers:')
        input1 = list(map(int,var1.split(' ')))
        am.mean(input1)
        gobacktomenu(2)
    elif menuenter ==2:
        var2 = input('Enter numbers:')
        input2 = list(map(int,var2.split(' ')))
        am.mad(input2)
        gobacktomenu(2)
    elif menuenter ==3:
        am.squareroot(int(input("Enter number: ")))
        gobacktomenu(2)
    elif menuenter ==4:
        am.power(int(input("Enter number to power: ")), int(input("Enter power number: ")))
        gobacktomenu(2)
    elif menuenter ==6:
        menu3()
    elif menuenter ==5:
        gobacktomenu(1)
    else:
        gobacktomenu(2)

def menu1():
    print("{-----------------Page 1 -----------------}")
    print("|||||||||||||||||||||||||||||||||||||||||||")
    print("{--1--- Add ------}||||{--2--- Subtract --}")
    print("{--3--- Multiply -}||||{--4--- Divide ----}")
    print("{----------------------- 6 -->>>  Page 2 -}")
    menuenter = int(input("Enter: "))
    if menuenter == 1:
        m.add(int(input("Enter first Number: ")), int(input("Enter second Number: ")))
        gobacktomenu(1)
    elif menuenter ==2:
        m.subtract(int(input("Enter first Number: ")), int(input("Enter second Number: ")))
        gobacktomenu(1)
    elif menuenter ==3:
        m.multiply(int(input("Enter first Number: ")), int(input("Enter second Number: ")))
        gobacktomenu(1)
    elif menuenter ==4:
        m.divide(int(input("Enter first Number: ")), int(input("Enter second Number: ")))
        gobacktomenu(1)
    elif menuenter ==6:
        menu2()
    else:
        gobacktomenu(1)