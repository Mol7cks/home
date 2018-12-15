import numpy as np
def OR(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.4
    tmp = np.sum(w*x) + b
    if tmp<=0:
        return 0
    else:
        return 1

a=OR(0,0)
b=OR(1,0)
c=OR(0,1)
d=OR(1,1)

print(a)
print(b)
print(c)
print(d)
