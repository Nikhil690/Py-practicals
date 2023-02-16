t1 = (1,2,5,7,9,2,4,6,8,10)
t2 = (11,13,15)
half = len(t1) // 2

first_half = t1[:half]
second_half = t1[half:]
even_tup = ()
print(first_half,"\n",second_half)

for i in t1:
    if i % 2 == 0:
        even_tup += (i,)

added_tuple = t1 + t2

print(even_tup)
print(added_tuple)
print(int(max(added_tuple)))
print(int(min(added_tuple)))
