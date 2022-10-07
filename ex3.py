import numpy as np

#random matrix 3x3
a = np.empty((3,3), np.uint16)
print(a)

#square diagonal matrix 5x5
b = np.identity(5)
print(b)

#custom size diagonal matrix with diagonal offset
c = np.eye(2,3, k=1)
print(c)

#only zeros 3x3
d = np.zeros((3,3))
print(d)

#only ones 4x4
e = np.ones((4,4))
print(e)

#custom size matrix with custom value
f = np.full((5,5), 32)
print(f)
