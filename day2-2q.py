def checkyear(year):
    year=int(year)
    if(year<1 ):
        print('enter a valid year')
    elif(year%4==0 and year%100!=0):
        print("leap year")
    elif(year%400==0):
        print('leap year')
    else:
        print("not leap year")
    return year
year=(input('enter the year'))
for i in year:
    if i ==".":
        print("enter a valid year")
print(checkyear(year))
