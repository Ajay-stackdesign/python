# 3. Write a Python program to insert items into a list in sorted order.

list = []
def insert_items(item):
    for x in item:
        list.insert(1,x);
    list.sort();
    print(list);

list1 =[25,45,36,47,69,48,68,78,14,36];
insert_items(list1)

# Given a list, write a Python program to swap first 
# and last element of the list.
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# newlist = [0]
def swaping_numbers(list):
    # for x in list:
    # size = len(list);
    # temp = list[0];
    # list[0] = list[ size - 1 ];
    # list[ size -1 ] = temp
    # print(list)
    # list[0] = list[-1] 
    # list[-1] = 
    list5 = list[-1]
    print(list5)


list2 = [12,35,9,56,24];
swaping_numbers(list2);

sre = [1, 2, 3, 5, 4];
a,*b = sre

print(a),print(b)
# ,print(c),print(d),print(e)



