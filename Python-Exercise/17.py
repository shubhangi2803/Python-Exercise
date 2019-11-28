l=[]
while True:
    s=input()
    v=s.split(' ')
    if s:
        l.append(v)
    else:
        break;
a=[]
b=[]
bal=0
for i in range(len(l)):
    a.append(l[i][0])
    b.append(l[i][1])
for i in range(len(a)):
    if a[i]=='D':
        bal+=int(b[i])
    if a[i]=='W':
        bal-=int(b[i])
print(bal)
