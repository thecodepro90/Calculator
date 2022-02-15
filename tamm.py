class Math:
    def add(a,b):
        print(f"{a} + {b} = {a + b}")

    def subtract(a,b):
        print(f"{a} - {b} = {a - b}")

    def divide(a,b):
        print(f"{a} / {b} = {a / b}")

    def multiply(a,b):
        print(f"{a} * {b} = {a * b}")

class Advancedmath(Math):
    def mean(a):
        mean = sum(a)/len(a)
        print(f"Mean: {mean}")
    
    def mad(a):
        mean = sum(a)/len(a)
        absoluteDeviation = []
        for eachValue in a:
            absoluteDeviation.append(abs(eachValue - mean))
            eachValue += 1

        mad = sum(absoluteDeviation)/len(absoluteDeviation) 
        print(f"Mad:{mad}")

    def squareroot(a):
        square_root = a**(1/2)
        print(f"Square root of {a} is {square_root}")

    def power(a,b):
        print(f"{a}^{b} = {pow(a,b)}")

    def percent(a,b):
        print(f"{a} % of {b} is {a * b / 100}")
        


class Trigonomitry: 
    def pathagoreantriple(a,b,c):
        list1 = []
        list1.append(a)
        list1.append(b)
        list1.append(c)
        largestnumber = max(list1)
        a1 = pow(a,2)
        b1 = pow(b,2)
        c1 = pow(largestnumber, 2)
        if a1 + b1 == c1:
            print("True")
        else:
            print("False")

    def pathagoreanunkownvar(leg1,leg2,unknownside):
        if unknownside == "a":
            side_b = leg1
            side_c = leg2
            side_find = (side_c**2 - side_b**2)**(1/2)
            print(f"The unknown side is {side_find}")
        elif unknownside == "b":
            side_a = leg1
            side_c = leg2
            side_find = (side_c**2 - side_a**2)**(1/2)
            print(f"The unknown side is {side_find}")
        else:
            side_a = leg1
            side_b = leg2
            side_find = (side_a**2 + side_b**2)**(1/2)
            print(f"The unknown side is {side_find}")