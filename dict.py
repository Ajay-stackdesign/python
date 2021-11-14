# accessing the key values in dictionary
dict = {
    "name": "ajay",
    "class": 9,
    "age" : 10
}
print(dict)

# updating values in dictionaries

dict["name"]="sahani";
print(dict)

# delete values in dictonaries

del dict["class"];
print(dict)

# build-in dictionaries functions and methods:
# 1)len(dict)

print(len(dict))

# str(dict):

print(str(dict))

# type(variable)


print(type(dict))

# python dictionaries method:
# dict.clear();
# remove all the element in the of dictionaries:

print(dict.clear())

dict={
    "name":"ajay",
    "class": 10,
    "age": 6
}
print(dict)

# dict.copy();
# returns a shallow copy of dictoanries

print(dict.copy())

# dictionaries fromKeys() method.
# the method fromKeys() creates a new dictioanrieswith keys from seq and values set to value.
# syntax : dict.fromKeys(seq,[value])

# dictionaries get() method:
# the method get() returns a value for the given key.if the key is not avialable then it returns it defaullt value none:

print(dict.get("email","not found"))

# Dictonary items() method:
# the method items() rerurns a list of dicts(key,value)tuple pairs:

print(dict.items())

# dictionary key():
# the method return the key avialabkle in the dictonaries
# this mwthod returns a list of all the available keys inn the dictonaries

print(dict.keys())

print(dict.pop("name"))

for i in dict.get("class"):
    print(i);