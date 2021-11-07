# it can print n number of iteration

def sqaure_number(number):
    squarenNumber = [];
    for x in number:
        squarenNumber.append(x+x)
    return squarenNumber;


number = [1,2,4,5];
result = sqaure_number(number)
print(result)

