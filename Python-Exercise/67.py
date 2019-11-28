def fibo(n):
    if n==0:
        return(0)
    if n==1:
        return(1)
    elif n>1:
        return(fibo(n-1)+fibo(n-2))
n=int(input())
##l=[]
##for i in range(0,n+1):
##    l.append(fibo(i))
##    l[i]=str(l[i])
##print(','.join(l))
t=[str(fibo(x)) for x in range(0,n+1)]
print(','.join(t))
