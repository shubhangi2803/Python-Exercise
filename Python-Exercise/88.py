l=[12,24,35,70,88,120,155]

'''l=filter(lambda x: x%35!=0,l)
print(list(l))'''

l=[x for x in l if x%35!=0]
print(l)

'''for i in range(len(l)-1,-1,-1):
    if l[i]%5==0 and l[i]%7==0:
        l.remove(l[i])
print(l)'''

##p=[]
##for i in l:
##    if i%7==0 and i%5==0:
##        p.append(i)
##for i in p:
##    for j in l:
##        if j==i:
##            l.remove(j)
##print(l)

