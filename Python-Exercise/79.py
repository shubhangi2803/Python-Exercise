import random
l=[]
for i in range(0,5):
    l.append(random.choice([i for i in range(100,201) if i%2==0]))
print(l)
#print(random.sample([i for i in range(100,201) if i%2==0],5))
