N1 = int(input("Enter N:"))
l1 = []
for i in range(0, N1):
    ele = int(input("Enter element: "))  
    l1.append(ele)     
print(l1)

N2 = int(input("Enter N:"))
l2 = []
for i in range(0, N2):
    ele = int(input("Enter element: "))  
    l2.append(ele)     
print(l2)

l3= [ (i,j) for i,j in zip(l1,l2)]

print(l3)
