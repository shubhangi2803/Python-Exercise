a=input()
l=[]
for i in range(len(a)):
    if i%2==0:
        l.append(a[i])
v=''.join(l)
print(v)
