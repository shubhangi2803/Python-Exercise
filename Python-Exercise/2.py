n=int(input("Enter a number : "))
fact=1
if n==0:
    print(1)
else:
    for i in range(n,1,-1):
        fact*=i
    print(fact)
