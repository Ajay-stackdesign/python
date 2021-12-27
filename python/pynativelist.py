# list1 = [100, 200, 300, 400, 500]

# list2 = list1[::-1]
# print(list2)


# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# for i,j in list(zip(list1,list2)):
#     print(i+j)

# join = [x+j for x,j in zip(list1,list2)]
# print(join) 

numbers = [1, 2, 3, 4, 5, 6, 7]
length = len(numbers)

multiply = [x*x for x in range(1,length + 1)]
print(multiply)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

join = [x+y for x,y in zip(list1,list2)]
print(join)

    
