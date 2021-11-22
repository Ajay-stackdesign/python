# # for x  in range(1,11,7+1):
# #     print(x)

# # # Print First 10 natural numbers using while loop

# # def natural_number():
# #     num = 1
# #     while num < 11 :
# #         print(num);
# #         num = num +1

# # natural_number()

# # #  Print the following pattern
# # # 1 
# # # 1 2 
# # # 1 2 3 
# # # 1 2 3 4 
# # # 1 2 3 4 5
# # def pattern():
# #     for i in range(1,6,1):
# #         for j in range(1,i+1):
# #             print(j,end=" ")

# #         print("")

# # pattern()


# # def pattern1():
# #     for i in range(1,6,1):
# #         for j in range(1,i+1):
# #             print(j,end=" ");
# #         print("")

# # pattern1()


# # # def sumNumber():
# # #     user = int(input("enter the number"))
# # #     sum = 0 ;
# # #     num = 1
# # #     while num > user :
# # #         avg = sum + num;
# # #         print(sum)
    
# # # sumNumber()


# # # print multiplation of 2 

# # #  step 1: 


# # for i in range(2,3):
# #     for j in range(1,11):
# #         result = i*j
# #         print(i,"*",j,"=", result)




    


# '''Challenge #1: Iterate through every 
# number in a list to separate out even and odd numbers. 
# Identify possible outlier values as well.'''

# # my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
# # Out:
# # Even numbers [2, 4, 6, 32, 2, 4]
# # Odd numbers [1, 3, 5, 7, 21, 33]
# # outliers [100, 110]

# from typing import Counter


# def find_out(list):
#     output =[];
#     even = [];
#     odd = [];
#     for x in list:
#         if x > 90 :
#             output.append(x);
            
#         elif x % 2 == 0 :
#             even.append(x);
            
#         else:
#             odd.append(x);
           
#     print(even)
#     print(odd)
#     print(output)     
        
# list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4];

# find_out(list);
# # print(result)

# # Challenge #2: Find the sum of all numbers in a list

# number = int(input("enter the number"));
# def sum_number():
#     sum =0
#     for x in range(0,number ):
#         sum += x;
#     print(sum);

# sum_number();

# num_sum = 0
# for i in list:
#     num_sum += i
# print('Sum of the elements in the list', num_sum) 


# # Challenge 3: Calculate the sum of even numbers in a list

# def even_number(list):
#     even_num = []
#     for x in list:
#         if x % 2 == 0:
#             even_num.append(x);


#     sum = 0
#     for i in even_num:
#         sum += i;
#     print(sum)

# my_list = [10,20,20,1,2,3]
# even_number(my_list)

# # Challenge 4: Count the number of even numbers in a list




# count = 0
# def count_number(list):
#     for x in list:
#         if list[x] % 2 == 0:
#             Counter += list[x]
    
#     print(count)
        
# counter = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4];
# count_number(Counter)


# def even_number(list):
#     for x in range(len(list)):
#         if list[x] % 2 == 0 :
#             count =count + 1;
#     print(count) 

# list10 = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4];
# even_number(list10);
    
'''from collections import Counter


# my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4];
sum = 0;
def even_number(my_list):
    global sum
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            sum +=1
    print('The count of even numbers in the list', sum)

list10 = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]; 
even_number(list10)


# Challenge 5: Calculate the cumulative sum of all elements in a list

cummulative = [];
initial = 0;
def cummalative_number(list):
    global initial
    for x in list:
        initial +=x;
        cummulative.append(initial);
    print(cummulative)

list10 = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]; 
cummalative_number(list10)

def func():
    for i in range(5):
        print(i)
func();

for i in range(10,15):
    for j in range(10,15):
        print(i*j);

# Write a program to print first 10 natural number.
for x in range(1,11):
    print(x);

# Write a program to print first 10 even numbers.
for i in range(2,21):
    if i % 2 == 0:
        print(i)

number = int(input("enter the number"))

for i in range(0,number):
    if i % 2 != 0:
        print(i);'''
# even = []
user = int(input("enter the number"))
even = []
# add =[]
for i in range(1,user,1):
    if i % 2 == 0:
        even.append(i)
        
        # even.append(i)
even.reverse()
print(even)

for i in (1,11):
    print(i)


for i in range(1,5):
    for j in range(1,1+i):
        print(j,end="");
    print(" ")




        














        






