class person:
    def getgender(self):
        pass
        #print("Unknown")
class male(person):
    def getgender(self):
        print("Male")
class female(person):
    def getgender(self):
        print("Female")
p=person()
p.getgender()
q=male()
q.getgender()
r=female()
r.getgender()
