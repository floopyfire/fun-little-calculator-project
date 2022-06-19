import operators as op

loop = True
while loop:
    print("------------------------------\nBasic digital calculator\nMade by floopy\n\
------------------------------\nSelect one of the operations below to continue.\n1. Addition\n2. Subtraction\
\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Roots\n7. Factorialization")
    sel = int(input(""))
    while 1 > sel or 7 < sel:
        print("Please enter a valid answer.\n1. Addition\n2. Subtraction\
    \n3. Multiplication\n4. Division\n5. Exponentiation\n6. Roots\n7. Factorialization")
        sel = int(input())
    while sel == 1:
        conf = input("Are you sure you want to add? (Y/N)\n")
        while conf.lower() != "n" and conf.lower() != "y":
            conf = input("Please select a valid answer. (Y/N)\n")
        if conf.lower() == "y":
            op.add()
            exit(0)
        print("Alright, going back.")
        break
    while sel == 2:
        conf = input("Are you sure you want to subtract? (Y/N)\n")
        while conf.lower() != "n" and conf.lower() != "y":
            conf = input("Please select a valid answer. (Y/N)\n")
        if conf.lower() == "y":
            op.sub()
            exit(0)
        print("Alright, going back.")
        break
    while sel == 3:
        conf = input("Are you sure you want to multiplicate? (Y/N)\n")
        while conf.lower() != "n" and conf.lower() != "y":
            conf = input("Please select a valid answer. (Y/N)\n")
        if conf.lower() == "y":
            op.mul()
            exit(0)
        print("Alright, going back.")
        break
    while sel == 4:
        conf = input("Are you sure you want to divide? (Y/N)\n")
        while conf.lower() != "n" and conf.lower() != "y":
            conf = input("Please select a valid answer. (Y/N)\n")
        if conf.lower() == "y":
            tp = int(input("Would you like to do:\n1. Division with remainder (5/2 = 2)\n2. Division without\
remainder (5/2 = 2.5)\n"))
            while tp != 1 and tp != 2:
                tp = int(input("Please select a valid answer.\n1. Division with remainder (5/2 = 2)\n2.\
Division with remainder (5/2 = 2.5)"))
            if tp == 1:
                conf = input("Are your sure you want to divide with remainder? (Y/N)\n")
                while conf.lower() != "y" and conf.lower() != "n":
                    conf = input("Please input a valid answer (Y-> yes, N-> no)\n")
                if conf.lower() == "y":
                    op.divwi()
                    exit(0)
                break
            conf = input("Are your sure you want to divide without remainder? (Y/N)\n")
            while conf.lower() != "y" and conf.lower() != "n":
                conf = input("Please input a valid answer (Y-> yes, N-> no)\n")
            if conf.lower() == "y":
                op.divwo()
                exit(0)
            break
        print("Alright, going back.")
        break
    while sel == 5:
        conf = input("Are you sure you want to exponentiate? (Y/N)\n")
        while conf.lower() != "n" and conf.lower() != "y":
            conf = input("Please select a valid answer. (Y/N)\n")
        if conf.lower() == "y":
            op.exp()
            exit(0)
        print("Alright, going back.")
        break
    while sel == 6:
        conf = input("Are you sure you want to do a root? (Y/N)\n")
        while conf.lower() != "n" and conf.lower() != "y":
            conf = input("Please select a valid answer. (Y/N)\n")
        if conf.lower() == "y":
            op.root()
            exit(0)
        print("Alright, going back.")
        break
    while sel == 7:
        conf = input("Are you sure you want to factorialize? (Y/N)\n")
        while conf.lower() != "n" and conf.lower() != "y":
            conf = input("Please select a valid answer. (Y/N)\n")
        if conf.lower() == "y":
            op.fact()
            exit(0)
        print("Alright, going back.")
        break




