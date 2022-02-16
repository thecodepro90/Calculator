
def devmenu2():
    print("{----------------- Dev mode -----------------}")
    print("||||||||||||||||||||||||||||||||||||||||||||||")
    print("{--1 go back to calculator ---}|||||||||||||||")
    print("{---<<< Page 1 << 5 -------------------------}")
    devmenu1 = int(input("Enter: "))
    if devmenu1 == 1:
        from menu import menu1
        menu1()
    elif devmenu1 == 5:
        from devmenu import devmenu1
        devmenu1()
    else:
        from devmenu import devmenu2
        devmenu2()

def devmenu1():
    print("{----------------- Dev mode -----------------}")
    print("||||||||||||||||||||||||||||||||||||||||||||||")
    print("{--1- write note ---}||||{--2- read note ----}")
    print("{--3- read all notes}||||{--4- delete note --}")
    print("{-------------------------- 6 -->>>  Page 2 -}")
    devmode = int(input("Enter: "))
    if devmode ==1:
        file1 = open("notes.txt", "w")
        note = input("Enter note: ")
        file1.write(note)
        from devmenu import devmenu1
        devmenu1()
    elif devmode ==2:
        file1 = open("notes.txt", "r")
        rnote = int(input("Enter note to read: "))
        noteline = rnote - 1
        content = file1.readlines()
        print(content[noteline])
        from devmenu import devmenu1
        devmenu1()
    elif devmode ==3:
        file1 = open('notes.txt', 'r')
        Lines = file1.readlines()
        count = 0
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))
        from devmenu import devmenu1
        devmenu1()
    elif devmode ==4:
        with open(r"notes.txt", 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            lnote = int(input("Enter line: ")) - 1
            for number, line in enumerate(lines):
                if number not in [lnote]:
                    fp.write(line)
        from devmenu import devmenu1
        devmenu1()
    elif devmode == 6:
        devmenu2()
    else:
        from devmenu import devmenu1
        devmenu1()

def devmode():
    user = input("Enter username: ")
    if user =="John Lopez":
        passw = input("Enter Password: ")
        if passw =="JLIC":
            devmenu1()
        else:
            print("Wrong Password!")
            from devmenu import devmode
            devmode()
    else:
        print("Wrong Username!")
        from devmenu import devmode
        devmode()