class circle:
    def __init__(self,r):
        self.rad=r
    def area(self):
        return(3.14*self.rad*self.rad)
c1=circle(7)
c2=circle(14)
v=c1.area()
w=c2.area()
