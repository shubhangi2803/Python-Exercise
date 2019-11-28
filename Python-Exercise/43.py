t=tuple([1,2,3,4,5,6,7,8,9,10])
l=[]
for i in range(len(t)):
    if t[i]%2==0:
        l.append(t[i])
tu=tuple(l)
print(tu)
