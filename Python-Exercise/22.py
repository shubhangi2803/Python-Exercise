s=input()
p=s.split(' ')
p.sort()
new=[]
for x in p:
    if x not in new:
        new.append(x)
for i in range(0,len(new)):
    print(new[i],':',s.count(new[i]),sep="")
    
    

