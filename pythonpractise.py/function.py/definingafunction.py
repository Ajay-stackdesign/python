# # defining a function

# def func():
#     result = "the strinng tpo be used"
#     print(result)

# # func();

# # calling a function:
# # defining a function gives it a name

# def func():
#     result = "this is me"
#     print(result)

# func()

# # // pass by value vs value
# def change(list):
#     print("print my list:", list)
#     list[2] = 500;
#     print(list)

# list = [10,20,30]
# change(list)

# print(list)


# def checking():
#     list9 = [1,2,3,4,5,6,7];
#     size = len(list9);
#     check = size-1 
#     print(check);

# checking()



# def a(b):
#     print(b)
# a(5);

# print(list)

# # required arguments :

# def printMe(str):
#     print(str)

# printMe()

# # 

# def swapList(newList):
#     size = len(newList)
     
#     # Swapping
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp
     
#     return newList
     
# # Driver code
# newList = [12, 35, 9, 56, 24]
 
# print(swapList(newList))

# new = [1,2,3]
# size = len(new);
# newlist = new[size-1];
# print(newlist)

def swaping_number(newlist):
    # size = len(newlist)

    temp = newlist[0];
    newlist[0] = newlist[2];
    newlist[2] = temp;

    return newlist;

newlist = [1,2,3];

sum = swaping_number(newlist)
print(sum)
