a=input()
vd=a.split(' ')
mylist=list(dict.fromkeys(vd))
final=sorted(mylist)
for s in final:
    print(s,end=' ')
