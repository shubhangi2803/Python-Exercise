#x+y=35
#(2*x)+(4*y)=94
for x in range(0,36):
    for y in range(0,36):
        if x+y==35 and (2*x)+(4*y)==94:
            print("Chickens: ",x)
            print("Rabbit: ",y)
