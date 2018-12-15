import numpy as np
def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp<=0:
        return 0
    else:
        return 1

a=AND(0,0)
b=AND(1,0)
c=AND(0,1)
d=AND(1,1)

print(a)
print(b)
print(c)
print(d)
