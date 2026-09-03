import numpy as np
rng = np.random.default_rng()
hit=0;
fail=0;
for i in range(1000000):
    a = rng.integers(low=1,high=7,size=5)
    if((a[0]==6 and a[1]!=6 and a[2]!=6)  or (a[0]!=6 and a[1]!=6 and a[2]==6) or (a[0]!=6 and a[1]==6 and a[2]!=6)):
        hit+=1
    else:
        fail+=1
print("Hits",hit,"Fail",fail)
print("ratio",hit/(hit+fail))

    
