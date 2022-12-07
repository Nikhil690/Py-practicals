r = True
while r == True: 
    num = int(input("Enter number of rows: "))
    while num != 0:
        print("* "*(2*num - 1))
        num -= 1
    r = input("To run the code again just type yes: ")
    if r == "yes":
        r = bool(True)
    else:
        r = bool(False)
