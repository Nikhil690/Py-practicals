import cmath

print('this is my first program')
a = input('type your name: ')
print('Welcome', a)

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
