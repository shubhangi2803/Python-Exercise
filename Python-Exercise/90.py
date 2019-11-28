m=3
n=5
l=8
p=lambda m,n,l :[[[0 for k in range(l)]for j in range(n)]for i in range(m)]
s=p(3,5,8)

import numpy as np
a=np.zeros(((3,5,8)))
