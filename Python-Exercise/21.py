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
x=0
y=0
for i in range(len(l)):
    a.append(l[i][0])
    b.append(l[i][1])
for i in range(len(a)):
    if a[i]=='UP':
        y+=int(b[i])
    if a[i]=='DOWN':
        y-=int(b[i])
    if a[i]=='RIGHT':
        x+=int(b[i])
    if a[i]=='LEFT':
        x-=int(b[i])
import numpy as np
print(int(np.sqrt(x**2+y**2)))
    
