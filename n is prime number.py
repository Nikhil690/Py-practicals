r = True
while r == True:    
    userInput2 = input('Type natural number: ')
    
    userInput2 = int(userInput2)

    if userInput2 == 0:
            print(userInput2,'is not a prime number')
    elif userInput2 > 2:
            for i in range(2,userInput2):
                if userInput2 % 2 == 0:
                    print(userInput2, 'is not a prime number')
                    break
                else:
                    print(userInput2,'is prime number')
                    break
    elif userInput2 == 2:
                    print(userInput2,"is a prime number")
    else:
            print('0 is not a prime number')

r = input('To run the code again just type yes: ')
if r == "yes":
    r = bool(1)
else:
    r = bool(0)

