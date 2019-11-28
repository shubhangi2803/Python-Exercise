a=input()
v=a.split(' ')
l=[]
for i in range(len(v)):
    if v[i].isdigit()==True:
        l.append(v[i])
print(l)
