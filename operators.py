def add():
    nums = 0
    loop = True
    while loop:
        print("--------------------\nFormat selected: Addition")
        while nums > 5 or nums < 2:
            print("How many inputs would you like to use?\n2-> a+b\n3-> a+b+c\n4-> a+b+c+d\n5-> a+b+c+d+e")
            nums = int(input())
            if 6 > nums > 2:
                break
            print("Please enter a valid answer.")
        print(f"--------------------\nInputs selected: {nums}\n\
Enter valid inputs for the variables (5, 5.3)\n--------------------")
        while nums >= 0:
            a = float(input("a = "))
            nums -= 1
            b = float(input("b = "))
            r = a + b
            nums -= 1
            if nums == 0:
                break
            c = float(input("c = "))
            r = a + b + c
            nums -=1
            if nums == 0:
                break
            d = float(input("d = "))
            r = a + b + c + d
            nums -= 1
            if nums == 0:
                break
            e = float(input("e = "))
            r = a + b + c + d + e
            break
        print(f"Your result is {r}, would you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")
        continue

def sub():
    nums = 0
    loop = True
    while loop:
        print("--------------------\nFormat selected: Subtraction")
        while nums > 5 or nums < 2:
            print("How many inputs would you like to use?\n2-> a-b\n3-> a-b-c\n4-> a-b-c-d\n5-> a-b-c-d-e")
            nums = int(input())
            if 6 > nums > 2:
                break
            print("Please enter a valid answer.")
        print(f"--------------------\nInputs selected: {nums}\n\
Enter valid inputs for the variables (5, 5.3)\n--------------------")
        while nums >= 0:
            a = float(input("a = "))
            nums -= 1
            b = float(input("b = "))
            r = a - b
            nums -= 1
            if nums == 0:
                break
            c = float(input("c = "))
            r = a - b - c
            nums -=1
            if nums == 0:
                break
            d = float(input("d = "))
            r = a - b - c - d
            nums -= 1
            if nums == 0:
                break
            e = float(input("e = "))
            r = a - b - c - d - e
            break
        print(f"Your result is {r}, would you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")
        continue

def mul():
    nums = 0
    loop = True
    while loop:
        print("--------------------\nFormat selected: Multiplication")
        while nums > 5 or nums < 2:
            print("How many inputs would you like to use?\n2-> ab\n3-> abc\n4-> abcd\n5-> abcde")
            nums = int(input())
            if 6 > nums > 2:
                break
            print("Please enter a valid answer.")
        print(f"--------------------\nInputs selected: {nums}\n\
Enter valid inputs for the variables (5, 5.3)\n--------------------")
        while nums >= 0:
            a = float(input("a = "))
            nums -= 1
            b = float(input("b = "))
            r = a * b
            nums -= 1
            if nums == 0:
                break
            c = float(input("c = "))
            r = a * b * c
            nums -=1
            if nums == 0:
                break
            d = float(input("d = "))
            r = a * b * c * d
            nums -= 1
            if nums == 0:
                break
            e = float(input("e = "))
            r = a * b * c * d * e
            break
        print(f"Your result is {r}, would you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")
        continue

def divwi():
    loop = True
    while loop:
        print("--------------------\nFormat selected: Division with remainder (a/b)")
        print("Enter valid inputs for the variables (5, 5.3)\n--------------------")
        a = float(input("a = "))
        b = float(input("b = "))
        q = a // b
        r = a % b
        print(f"Your quotient is {q}.\nYour remainder is {r}.\nWould you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")
        continue

def divwo():
    loop = True
    while loop:
        print("--------------------\nFormat selected: Division without remainder (a/b)")
        print("Enter valid inputs for the variables (5, 5.3)\n--------------------")
        a = float(input("a = "))
        b = float(input("b = "))
        r = a / b
        print(f"Your result is {r}, would you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")
        continue

def exp():
    loop = True
    while loop:
        print("--------------------\nFormat selected: Exponentiation (a^b)")
        print("Enter valid inputs for the variables (5, 5.3)\n--------------------")
        a = float(input("a = "))
        b = float(input("b = "))
        r = a ** b
        print(f"Your result is {r}, would you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")
        continue

def root():
    loop = True
    while loop:
        print("--------------------\nFormat selected: Root (root of 'a' with index 'b')")
        print("Enter valid inputs for the variables (5, 5.3)\n--------------------")
        a = float(input("a = "))
        b = float(input("b = "))
        r = a ** (1/b)
        print(f"Your result is {r}, would you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")
        continue

def fact():
    loop = True
    while loop:
        print("--------------------\nFormat selected: Factorialization (a!)")
        print("Enter only integers for the variable 'a' (5, 3)\n--------------------")
        a = int(input("a = "))
        if a == 0:
            a = 1
        else:
            for n in range(2, a):
                a *= n
        print(f"Your result is {a}, would you like to do another operation? (Y/N)")
        reset = input()
        while reset != "y" and reset != "n":
            print("Please enter a valid answer (Y->yes, N->no)")
            reset = input()
        if reset.lower() == "n":
            return print("Got it.\n--------------------")