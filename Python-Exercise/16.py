v=input()
q=v.split(',')
s=[]
for i in q:
    s.append(int(i))
r=[]
for i in range(0,len(s)):
    if s[i]%2!=0:
        r.append(s[i]*s[i])
for i in range(len(r)):
    r[i]=str(r[i])
print(','.join(r))
