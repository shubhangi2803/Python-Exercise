s=input()
inp=s.split(',')
#print(inp)
new=[]
for i in range(len(inp)):
    a=0
    b=0
    c=0
    d=0
    j=inp[i]
    if len(j)>=6 and len(j)<=12:
        for k in range(len(j)):
            if j[k].isalpha()==True and j[k].islower()==True:
                a+=1
            if j[k].isdigit()==True:
                b+=1
            if j[k].isalpha()==True and j[k].isupper()==True:
                c+=1
            if j[k]=='$' or j[k]=='#' or j[k]=='@':
                d+=1
    if  a!=0 and b!=0 and c!=0 and d!=0:
        new.append(j)
print(','.join(new))
#print(new)
