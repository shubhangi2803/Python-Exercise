#import sys
#Q=sys.stdin.read()
#print(Q.upper())

line=[]
while True:
    s=input()
    if s:
        line.append(s.upper())
    else:
        break;
for l in line:
    print(l)
