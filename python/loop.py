for x  in range(1,11,7+1):
    print(x)

# Print First 10 natural numbers using while loop

def natural_number():
    num = 1
    while num < 11 :
        print(num);
        num = num +1

natural_number()

#  Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
def pattern():
    for i in range(1,6,1):
        for j in range(1,i+1):
            print(j,end=" ")

        print("")

pattern()


def pattern1():
    for i in range(1,6,1):
        for j in range(1,i+1):
            print(j,end=" ");
        print("")

pattern1()


# def sumNumber():
#     user = int(input("enter the number"))
#     sum = 0 ;
#     num = 1
#     while num > user :
#         avg = sum + num;
#         print(sum)
    
# sumNumber()


# print multiplation of 2 

#  step 1: 


for i in range(2,3):
    for j in range(1,11):
        result = i*j
        print(i,"*",j,"=", result)

    


