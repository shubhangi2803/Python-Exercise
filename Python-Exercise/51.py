class American:
    @staticmethod
    def nationality():
        print("American")
class NewYorker(American):
    def __init__(self,name):
        self.name=name
ny=NewYorker("Sam")
print(ny.name)
ny.nationality()
