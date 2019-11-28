#class CustomError(Exception):
#    pass
#raise CustomError("ERRORRRR ERRORRRR !!!!")

class MyError(Exception):
    def __init__(self,msg):
        self.msg=msg
error=MyError(" Something is wrongg !! ")
print(error)
