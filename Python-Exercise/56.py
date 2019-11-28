def fun():
    return(5/0)
try:
    fun()
except(ZeroDivisionError):
    print("Heyyyy ! Check your expression")
