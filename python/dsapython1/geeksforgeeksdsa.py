# Python Program to find largest element in an array
# Difficulty Level : Easy
# Last Updated : 04 Jan, 2018
# Given an array, find the largest element in it.

# Input : arr[] = {10, 20, 4}
# Output : 20

# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100

# step 1 : defining a function 
# step 2 : to check whetherr the number in the list is in order or not.
# step 3 : if it is not in order then order it using sort method 
# step 4 : if its gets in order then print the last index.

# import math

# def largest_number(arr):
#     for i in range(len(arr)):
#         sum = (arr[i])
#         print(max(sum))



# arr = [10,5,20]
# largest_number(arr)

import math

def largest_number(arr):
    for i in range(0,arr):
        print(arr[i])

arr = [1,2,3]
largest_number(arr)