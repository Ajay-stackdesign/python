# list = ["banana","apple","orange","mango","cherry"]
# print(list[-1])

# if "cherry" in list:
#     print("yes");
# else:
#     print("no")
list = ["banana","apple","orange","mango","cherry"]
for x in list:
    if list[0] == "banana":
        print("yes")
    else:
        print("no")

list1 = [1,2,3,4]
list2 = [5,6,7,8]

my_list = list1 + list2;
print(my_list)

my_list1 = [1,2,3,4]
print(my_list1[::-1])


working_list = [10,20,30,40];

original_list = [i*i for i in working_list];
print(original_list);