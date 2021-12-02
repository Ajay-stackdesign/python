from itertools import product, repeat

a = [1, 2]
b = [3]

prod = product(a,b,repeat=2) #it will repeat like (1,3,1,3),(1,3,2,3),(2,3,1,3),(2,3,2,3)
# and without repeat is like (1,3),(2,3)  prod = product(a,b)
print(list(prod))

from itertools import permutations

a = [1,2,3]

b = permutations(a,3) # here 3 stands for length.
print(list(b))

from itertools import combinations, combinations_with_replacement

x = [1,2,3,4]
y = combinations(x,2)
print(list(y))

comb_wr = combinations_with_replacement(x,2)
print(list(comb_wr))


from itertools import accumulate
import operator

p = [1,2,3,4]
q = accumulate(p, func=operator.mul)
print(list(q))  #it will increase the value in addition addition order a+b a+b+c a+b+c+d