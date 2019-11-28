def fun(n):
    if n==0:
        return(0)
    elif n>0:
        return(fun(n-1)+100)
v=int(input())
s=fun(v)
print(s)
