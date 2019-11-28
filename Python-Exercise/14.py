a=input()
c=0
d=0
for i in range(len(a)):
    if a[i].isupper()==True:
        c+=1
    if a[i].islower()==True:
        d+=1
print("UPPER CASE ",c)
print("LOWER CASE ",d)
