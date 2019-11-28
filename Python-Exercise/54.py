class shape:
    def area():
        return(0)
class square(shape):
    def __init__(self,length):
        self.l=length
    def area(self):
        return(self.l*self.l)
s=int(input())
sq=square(s)
v=sq.area()
print(v)
