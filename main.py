import cmath

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/2*a
root2 = (-b+cmath.sqrt(d))/2*a

print('the roots are:')
print(root1)
print(root2)