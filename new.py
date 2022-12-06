import cmath

name = input('type your name: ')
print('Hello,', name)

print('type Q for quadratic equations and P to check the no. is prime or not')
ans =  input('')

if ans == "Q":
        a = 1
        b = 5
        c = 6

        d = (b**2) - (4*a*c)

        root1 = (-b-cmath.sqrt(d))/2*a
        root2 = (-b+cmath.sqrt(d))/2*a

        print('the roots are:')
        print(root1)
        print(root2)  
elif ans == 'P': 
    num = input('enter no.')
    num = int(num)
    if num > 1:
        for i in range(2,num):
            if num % 2 == 0 :
                print(num, 'is not a prime number')
                break
            else:
                print(num, 'is a prime number')
    else:
        print(num, 'is not prime')
