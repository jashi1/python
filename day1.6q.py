def maxarea(a):
    maxarea=0
    l=0
    r=len(a)-1
    while l<r:
        base=r-1
        print(base)
        height=min(a[l],a[r])
        print(height)
        area=base*height
        print(area)
        maxarea=max(area,maxarea)
        print(maxarea)
        if a[l]<a[r]:
            l+=1
        else:
            r-=1
            return maxarea
print(maxarea([1,5,4,3]))
'''print(maxarea([3,1,2,4,5]))
print(maxarea([1,8,6,2,5,4,8,3,7]))
print(maxarea([1,1])) 
print(maxarea([7,3]))'''
