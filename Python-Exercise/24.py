print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
def fact(j):
    '''This is a function to get factorial of a number'''
    s=1
    for i in range(2,j+1):
        s=s*i
    return(s)
print("Factorial : ",fact(5))
print(fact.__doc__)
