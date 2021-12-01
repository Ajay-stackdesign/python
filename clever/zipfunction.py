# list1 = [1,2,3,4,5]
# list2 = ["one","two","three","four""five"]

# zipped = list(zip(list1,list2))
# print(zipped)

# unzipp = list( zip(*zipped) )
# print(unzipp) 


list3 = [1,2,3,4]
li = ["ajay","sahani","list"]
zipp = list(zip(list3,li))
print(zipp)

unzipped = list( zip(*zipp) )
print(unzipped) 


l2 = [1,2,3,4,5]
l3 = ["one","two","three","four","five"]
l4 = [1,3,3.45,"hello",110.12]

# for li1,li2 in zip(l2,l3):
    # print(li1)
    # print(li2)

num1 = [(li1,li2,li3) for (li1,li2,li3) in zip(l2,l3,l4)]
print(num1)