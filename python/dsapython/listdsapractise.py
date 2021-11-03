# # Exercise 1: Reverse a given list in Python
# # aLsit = [100, 200, 300, 400, 500]
# # [500, 400, 300, 200, 100]

# alist = [100,200,300,400,500]
# alist.reverse()

# print(alist)

# # Exercise 2: Concatenate two lists index-wise
# # list1 = ["M", "na", "i", "Ke"]
# # list2 = ["y", "me", "s", "lly"]  input
# # ['My', 'name', 'is', 'Kelly']

# list1 =["M","na","i","Ke"]
# list2 =["y","me","s","lly"]

# for x in list1:
#     for y in list2:
#         result=x+y
#         print(result)

# # Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
# # aList = [1, 2, 3, 4, 5, 6, 7]
# # [1, 4, 9, 16, 25, 36, 49]

# def square_number(list2):
#     for x in list2:
#         print(x*x,end=" ")

# square_number([1,2,3,4,5,6,7])


# # Exercise 4: Concatenate two lists in the following order
# # list1 = ["Hello ", "take "]
# # list2 = ["Dear", "Sir"]
# # output ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# list4 = ["hello","take"]
# list5 = ["Dear","Sir"]

# list6 = [a+" "+b for a in list4 for b in list5]

# print(list6)

# # Exercise 6: Remove empty strings from the list of strings
# # list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # ["Mike", "Emma", "Kelly", "Brad"]
# list1 = ["Mike","","Emma","Kelly","","Brad"];
# # list1.remove("")
# # print(list1)
# output = ""
# for x in range(list1):
#     if list1[x] == output:
#         list2 = list1[x].re("")
#     print(list2)

    # Exercise 9: Given a Python list, find value 20 in the list, and if it is present,
    #  replace it with 200. Only update the first occurrence of a value
    # list1 = [5, 10, 15, 20, 25, 50, 20]
    # list1 = [5, 10, 15, 200, 25, 50, 20]

list = [5,10,15,20,25,50,20];
for x in list:
    print(x)
            
            
        






