num=int(input("enter a number: "))
I=[]
k=str(I)
for i in range(1,num+1):
    if(i%3==0):
        I.append("fuzz")
    elif(i%5==0):
        I.append("buzz")
    else:
        I.append(str(i))
    print(I)
        
    
