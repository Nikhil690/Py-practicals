while True:
    try:
        name = input("Please enter your name: ")
        if name.isalpha():
            print("hello",name)
            break
        elif not name.isalpha():
            print("you entered a wrong input. type again")
    except ValueError as error:
        print(error)
