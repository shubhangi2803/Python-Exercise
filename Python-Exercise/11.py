v=input()
q=v.split(',')
s=[]
for i in q:
    s.append(int(i))
p=[]
for i in q:
    p.append(int(i,2))
##print(p)
r=[]
for i in range(0,len(p)):
    if p[i]%5==0:
        r.append(s[i])
for i in range(len(r)):
    r[i]=str(r[i])
print(','.join(r))
