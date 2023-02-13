def delchar(s,c):
    if len(c)!=1:
        return s
    return s.replace(c,'')
s="123456s"
c="2"
print(delchar(s,c))

