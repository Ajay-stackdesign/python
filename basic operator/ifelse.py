#Write a JavaScript program that accept two integers and display the larger.

# step 1 : if a is greater than b print a is greater
# step 2 : if b is greater than a print b is greater

num1 = float(input("enter the number"))
num2 = float(input("enter the number"))

if num1 > num2 :
    print("a is greater")
else:
    print("b is greater")

    #A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
    #Ask user for their salary and year of service and print the net bonus amount.

salary = float(input("enter the number"))
years = float(input("enter the number"))

if years > 5 :
    print("net bons is:" , 0.5*years)
else:
    print("sorry your experience is less ")


#Take values of length and breadth of a rectangle from user and check if it is square or not.

length = input("enter the number")
breadth = input("enter the number")

if length == breadth :
    print("it is square")
else:
    print("it s not a square")

#Take two int values from user and print greatest among them.

one1 = int(input("enter the number"))
two2 = int(input("enter the number"))

if one1 > two2 :
    print("one1 is greater")
else:
    print("two is greater")

'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''


quantity = int(input("enter the quantity"))
 
if quantity*100 > 1000 :
    print((quantity*100)- (0.1*quantity/100))
else:
    print(quantity*100)

'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''

marks = float(input("enter the marks"))

if marks > 80 :
    print("A")
elif marks >60 and marks >=80  :
    print("B")
elif marks <50  and marks >=60 :
    print("C")
elif marks < 45 and marks >= 50 :
    print("D")
elif marks < 25 and marks >= 45 : 
    print("E")
else:
    print("F")
    

number = input()
if number<0:
  print (number*-1)
else:
  print (number)

'''Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400'''

year = input("enter the year")

if year% 4 == 0 :
    print("it is leap year")
elif year%4 != 0 :
    print("0ir is not leap year") 



