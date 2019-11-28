l=[5,6,77,45,22,12,24]
l=filter(lambda x: x%2!=0,l)
print(list(l))
##for i in range(len(l)-1,-1,-1):
##    if l[i]%2==0:
##        l.remove(l[i])
##print(l)
