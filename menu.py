from tamm import *
m = Math
am = Advancedmath
t = Trigonomitry

def devmenu():
    print("{----------------- Dev mode -----------------}")
    print("{--1- write note ---}||||{--2- read note ----}")
    print("{--3- read all notes}||||{--4- delete note --}")
    devmode = int(input("Enter: "))
    if devmode ==1:
        file1 = open("notes.txt", "w")
        note = input("Enter note: ")
        file1.write(note)
    elif devmode ==2:
        file1 = open("notes.txt", "r")
        rnote = int(input("Enter note to read"))
        noteline = rnote - 1
        content = file1.readlines()
        print(content[noteline])
    elif devmode ==3:
        file1 = open('notes.txt', 'r')
        Lines = file1.readlines()
 
        count = 0
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))
    elif devmode ==4:
        with open(r"notes.txt", 'r+') as fp:
            lines = fp.readlines()

            fp.seek(0)

            fp.truncate()

            lnote = int(input("Enter line: ")) - 1

            for number, line in enumerate(lines):
                if number not in [lnote]:
                    fp.write(line)


def devmode():
    user = input("Enter username: ")
    if user =="John Lopez":
        passw = input("Enter Password: ")
        if passw =="JLIC":
            devmenu()
        else:
            print("Wrong Password!")
    else:
        print("Wrong Username!")



def menu3():
    print("{------------------ Page 3 --------------------}")
    print("||||||||||||||||||||||||||||||||||||||||||||||||")
    print("{--1-- Percentage---}||||{-2 Pathagorean triple}")
    print("{--3- Pathagorean unkown var}|||||||||||||||||||")
    menu1 = input("Enter: ")
    if menu1 =="1":
        am.percent(int(input("Enter percent: ")), int(input("Enter number: ")))
    elif menu1 =="2":
        t.pathagoreantriple(int(input("Enter first side")), int(input("Enter second side")), int(input("Enter third side")))
    elif menu1 =="3":
        t.pathagoreanunkownvar()
    elif menu1 =="devmode":
        devmode()


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
        am.power(int(input("Enter number to power: ")), int(input("Enter power number: ")))
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