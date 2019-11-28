class num:
    def __init__(self,m):
        self.n=m
    def generator(self):
        for i in range(0,self.n+1):
            if i%7==0:
                print(i,end=' ')
m=int(input())
n=num(m)
n.generator()
