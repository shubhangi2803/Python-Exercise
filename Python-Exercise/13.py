a=input()
c=0
d=0
for i in range(len(a)):
    if a[i].isalpha()==True:
        c+=1
    if a[i].isdigit()==True:
        d+=1
print("LETTERS ",c)
print("DIGITS ",d)
