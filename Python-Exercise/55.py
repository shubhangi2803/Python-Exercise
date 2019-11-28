F=int(input("Force : "))
m=int(input("Mass : "))
if m==0:
    raise RuntimeError('Mass cannot be zero')
else:
    print("Acceleration : ",F/m)


#raise RuntimeError("ERROR ERROR ERROR")
