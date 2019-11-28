a=input()
l=[]
v=[]
for i in range(len(a)):
    if a[i] not in l:
        l.append(a[i])
for i in range(len(l)):
    v.append(a.count(l[i]))
for i in range(len(l)):
    print(l[i],",",v[i],sep="")
