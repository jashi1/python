def addBinary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    c = a + b
    return bin(c)[2:]
a=input("enter the binary number a: ")
b=input("enter the binary number b: ")
print(addBinary(a,b))
