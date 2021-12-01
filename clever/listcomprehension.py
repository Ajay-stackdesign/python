names = ["jeenifer","ajay","sahani","geeta"]


l = []
for person in names:
    l.append(person)
print(l)



names1 = ["ajay","sahani","geeta"]
x = [person for person in names1]

print(x)

name  = ["ajay","sahani"]

num = [ x for x in range(10) if x%2 == 0 ]
num.copy()
print(num)

fruits = [ "mango" if i%2 == 0 else "orange" for i in range(10)]
fruits.reverse()
print(fruits)

num1 = ["sahani","geeta","sahani"]
print([i + "ajay" for i in num1])

dict = {
    "Instellar": 9,
    "chalo": 8,
    "stellar": 5,
}

num = []