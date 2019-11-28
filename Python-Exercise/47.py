l=[1,2,3,4,5,6,7,8,9,10]

##r=list(filter(lambda x:x%2==0,l))
##n=map(lambda x:x*x,r)
##print(list(n))

##r=map(lambda x:x*x,l)
##n=filter(lambda x:x%2==0,r)
##print(list(n))

n=map(lambda x:x*x,list(filter(lambda x:x%2==0,l)))
print(list(n))
