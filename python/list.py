# # smallerNumber = 10
# # largestnumber = 20

# # if smallerNumber == largestnumber :
# #     print("nidhi sahani")
# # else:
# #     print("very good")

# # '''freinds = ["kevin","ajay","geeta","sahani"];
# # #[:] slice operator
# # tiny = [1,2,3,4]
# # print(freinds[0])
# # print(freinds[1:])
# # print(freinds[1:4])
# # print(freinds)
# # print(freinds+tiny)
# # freinds[1] = "geeta"
# # print(freinds)
# # freinds.append("geeta")
# # print(freinds)
# # freinds.insert(0,"geeta")
# # print(freinds)'''


# # # list practise sets 
# # #accessing value in lists
# # list=[1 ,2,3,4]
# # print([0])
# # print(list)

# # #list updating
# # list[2]=10
# # print(list)

# # # deleting list 


# # del list[2]
# # print(list)

# # list1 = [1,2,3]
# # list2 = [1,2,3]
# # print(list1+list2)

# # print(list1)




# # for i in range(0,5,1):
# #     print(i)


# #list practise :

# #list len() method 
# # list = [1,2,3,4]
# # print(len(list))

# # #list max() method

# # list1 = [1,2,3,4]
# # list2 = ["ajay","sahani","geeta"]
# # print(max(list1))
# # print(max(list2))

# # #list min() method

# # list3 = [1,2,3,4]
# # list4 = ["ajay","sahani","geeta"]
# # print(min(list3))
# # print(min(list4))

# # #list() this is used to convert tuple into list it also string into list

# str = "hello world"
# list6 = list(str)
# print(list6)



# # atuple = ("ajay","sahani","geeta")
# # list5=list(atuple)
# # print(list5)

# tuple = ("ajay","sahni")
# list5 =list(tuple)
# print(list5)


# list7 = ["ajay","sahani"]
# para = list7.append("geeta")
# print(list7)

# list8 = ["ajay","sahani","ajay"]
# para1 = list8.count("ajay")


# print(para1)

#extend list

# friend=["ajay","sahani"]
# lucky = ["geeta","sahani"]
# friend.extend(lucky)
# print(friend)

#insert() 
# list11 = ["ajay","sahani"]
# list11.insert(0,"geeta")
# print(list11) 

#remove
# list11.remove("geeta")
# print(list11)

#clear()
# list11.clear()
# print(list11)

#pop() : remove the elementfrom the last i  a list
# list12 =[1,2,3,4];
# list12.pop()
# print(list12)


# list13 = ["ajay","sahani"]
# print(list13.index("ajay"))

# list14 = [10 ,20 ,30 ,5,3,10,2]
# # list14.sort()
# # print(list14)


# list14.reverse()
# print(list14)

# list14.copy()
# print(list14)



#Find all of the numbers from 1–1000 that are divisible by 8

# num = [x for x in range(1,1000) if x%8==0]
# print(num)


# a = [x for x in range(2)]
# print(a)

# matrix = [[x*y*z for x in range(1)] for y in range(1) for z in range(2)]
# print(matrix)
list1 = [1,2]
list = [2,4,6,8,10];
list.append(list1)
list.reverse();
print(list)