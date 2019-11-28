import math
def binary_search(a,v):
    l=0
    u=len(a)-1
    index=-1
    while u>=l and index==-1:
        m=int((u+l)/2)
        if a[m]==v:
            index=m
        elif a[m]<v:
            l=m+1
        else:
            u=m-1
    return(index)
a=[1,2,3,4,5,6,7,8,9,10]
v=int(input("Enter the value to be searched : "))
index=binary_search(a,v)
if index==-1:
    print("Element not found !")
else:
    print("Element found at index : ",index)
