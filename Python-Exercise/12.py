l=[]
for i in range(1000,3001):
    c=0
    p=i
    while i>0:
        s=i%10
        i=i//10
        if s%2==0:
            c+=1
    if c==4:
        l.append(p)
for i in range(len(l)):
    l[i]=str(l[i])
print(','.join(l))
