l=[12,24,35,70,88,120,155]
##for i in range(len(l)-1,-1,-1):
##    if i%2==0:
##        del(l[i])
##print(l)
l=[x for x in l if l.index(x)%2!=0]
print(list(l))
