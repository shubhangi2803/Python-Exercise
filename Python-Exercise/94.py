l=[12,24,35,24,88,120,155,88,120,155]
#l= list(dict.fromkeys(l))
#print(l)

f=[]
for i in l:
    if i not in f:
        f.append(i)
l=f
print(l)
