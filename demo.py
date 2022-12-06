import cmath

print('this is my first program')
a = input('type your name: ')
print('Welcome', a)

print('type the function name which do you want to use')
print('''type \'Q\' or \'q\' to solve quadratic equation.
and for check prime number type \'p\' or \'P\'.''')

userInput = input()

if userInput == 'Q':
    n1 = input('type number with x^2: ')
    n2 = input('type number with x: ')
    n3 = input('type constant number: ')

    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    d = (n2**2) - (4*n1*n3)

    if d == 0:
        print('this equation has real root')

        root = (-n2-cmath.sqrt(d))/2*n1
        # print(d)
        print('a unique solution is: ')
        print(root)
    elif d > 0:
        print('this equation has two real and distinct roots')
        root1 = (-n2-cmath.sqrt(d))/2*n1
        root2 = (-n2+cmath.sqrt(d))/2*n1
        # print(d)
        print('the roots are:')
        print(root1)
        print(root2)
    else:
        # print(d)
        print('no real roots')
elif userInput == 'P':

    userInput2 = input('Type natural number: ')
    
    userInput2 = int(userInput2)

    if userInput == 0:
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
        print('this is a prime number')

else:
    print('run the code again')
