n=int(input())
##l=[]
##for i in range(0,n+1):
##    if i%5==0 and i%7==0:
##        l.append(i)
##for i in range(len(l)):
##    l[i]=str(l[i])
##print(','.join(l))
def GeneratorFunction(n):
    for i in range(0,n+1):
        if i%5==0 and i%7==0:
            yield(i)
x=GeneratorFunction(n)
c=list(x)
for i in range(len(c)):
    c[i]=str(c[i])
print(','.join(c))
