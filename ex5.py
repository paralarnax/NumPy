import numpy as np

#create vecror or matrix with increasing value
a = np.arange(10)
b = np.arange(5, 10)
c = np.arange(3, 8, 0.5)
print(a)
print(b)
print(c)

#create matrix with division of the range into equal parts
d = np.linspace(0, np.pi, 9).reshape(3,3)
print(d)

#create log vector with division of the range into equal parts
e = np.logspace(0,5,10,base=3)
print(e)

#create geometric progression vector
f = np.geomspace(1,125,4)
print(f)

#create a copy of a matrix
g = np.copy(d)
print(g)

#create matrix from function
def getRange(x,y):
    return 10 ** x + 2 * y
h = np.fromfunction(getRange, (3,3))
print(h)

#create vector from iterated object
i = np.fromiter('hello',dtype='U1')
print(i)

#create vector from string with separator
j = np.fromstring('1|2|3|4|5|6', dtype=np.int16, sep='|').reshape(2,3)
print(j)