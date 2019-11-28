l=[0,1,2,3,4,5,6]
l=[x for x in l if ((l.index(x) not in (0,4,5)))]
print(list(l))
