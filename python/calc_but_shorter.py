def calc():
    n1 = input("First number: ")
    op1 = input("First Operation: ")
    n2 = input("Second number: ")
    q1 = input("More? (y/n): ")

    if q1 == "n":
        print("Calculating...")
        ans1 = eval(n1 + op1 + n2)
        print(ans1)
    else:
        op2 = input("Second Operation: ")
        n3 = input("Third number: ")
        q2 = input("More? (y/n): ")
        if q2 == "n":
            print("Calculating...")
            ans2 = eval(n1 + op1 + n2 + op2 + n3)
            print(ans2)
        else:
            op3 = input("Third Operation: ")
            n4 = input("Fourth number: ")
            q3 = input("More? (y/n): ")
            if q3 == "n":
                print("Calculating...")
                ans3 = eval(n1 + op1 + n2 + op2 + n3 + op3 + n4)
                print(ans3)
            else:
                op4 = input("Fourth Operation: ")
                n5 = input("Fifth number: ")
                print("Calculating...")
                ans4 = eval(n1 + op1 + n2 + op2 + n3 + op3 + n4 + op4 + n5)
                print(ans4)


calc()