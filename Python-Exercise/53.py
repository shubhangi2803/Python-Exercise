class rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        return(self.l*self.b)
a=int(input("Length : "))
b=int(input("Breadth : "))
r1=rectangle(a,b)
print("Area : ",r1.area())
