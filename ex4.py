import numpy as np

#create matrix 1x4 from string
a = np.mat('1 2 3 4')
print(a)

#create matrix 2x2 from string
b = np.mat('1 2; 3 4')
print(b)

#create diagonal matrix with custom values
c = np.diag((3,4,5))
print(c)

#return diagonal part of matrix
d = np.diag(b)
print(d)

#create triangle matrix 4x4 with ones
e = np.tri(4)
print(e)

#create custom size triangle matrix with diagonal offset
f = np.tri(3,5,k=2)
print(f)

#create triange matrix from another matrix (use np.triu() to switch diagonal part)
g = np.tril(np.mat('1 2 3; 4 5 6; 7 8 9'))
print(g)

#create vandermond matrix
h = np.vander((1,2,3,4))
print(h)