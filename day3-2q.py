print("give a three digit number")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
print(d)
if (d[0]>=10 or d[1]>=10 or d[2]>=10):
    print ("invalid input")
else:
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if(i!=j&j!=k&k!=i):
                    print(d[i],d[j],d[k])
