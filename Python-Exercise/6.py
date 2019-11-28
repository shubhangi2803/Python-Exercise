import math
C=50
H=30
print("Enter the values of D : ")
D_val=(input().split(','),int)
##print("D :")
##print(D_val[0])
Q_val=[]
for i in range(len(D_val[0])):
    x=(2*C*int(D_val[0][i]))//H
    Q=int(math.sqrt(x))
    Q_val.append(str(Q))
print("Q :")
print(','.join(Q_val))
