import numpy as np
print("Enter the dimensions of matrix : ")
X,Y=(input().split(','))
X=int(X)
Y=int(Y)
A=[]
for i in range(0,X):
    B=[]
    for j in range(0,Y):
        B.append(i*j)
    A.append(B)
print(A)
