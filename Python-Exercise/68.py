##n=int(input())
##l=[]
##for i in range(0,n+1):
##    if i%2==0:
##        l.append(str(i))
##print(','.join(l))

def GeneratorFunction(n):
    for i in range(0,n+1):
        if i%2==0:
            yield(i)
n=int(input())
x=GeneratorFunction(n)
c=list(x)
for i in range(len(c)):
    c[i]=str(c[i])
print(','.join(c))
