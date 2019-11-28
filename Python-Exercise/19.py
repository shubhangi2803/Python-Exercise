from operator import itemgetter
l=[]
while True:
    s=input()
    v=s.split(',')
    if s:
        l.append(tuple(v))
    else:
        break
p=sorted(l,key=itemgetter(1,0,2))
