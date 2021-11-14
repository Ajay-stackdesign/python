# array python dsa

# stock_prices = [
#     [2,3,5,6],
#     [40,42,38,44],
#     [78,89,71,56]
# ]

# print(stock_prices[1])


# january 2200
# february 2350
# March 2600
# April 2130
#may 2190


# month = [2200,2350,2600,2130,2190]

# # print(month[1]-month[0])
# # print(month[0]+month[1]+month[2])
# # for i in month:
# #     if month[i]==200:
# #         print("spent 200 dollar")
# #     else:
# #         print("not spent") 

# lrt = month.append(1980)
# print(lrt)

heros = ["spider man","thor","hulk","iron man","captain america"]

print(len(heros))

heros.append("black panther")
print(heros)


heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
heros[1:3] = ["doctor strange"]
print(heros)

heros.sort()
print(heros)


# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

# number = int(input("enter the number: "))
# odd_number = []
# for x in range(1,max):
#     if x%2==1:
#         odd_number.append(x)

# print(odd_number)

max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)

number = int(input("enter the number :"))

odd_number = [];

for x in range(1 ,number):
    if x % 2 == 1 :
        odd_number.append(x)

print(odd_number)

list = [1,2,3,4]
list.reverse()
print(list)
