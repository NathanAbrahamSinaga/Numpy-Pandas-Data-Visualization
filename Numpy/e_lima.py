import numpy as np

n = [6, 7, 8]
n[0:2]
n[-1]

a = np.array([5,2,1,4,3])
a[0:2]
a[-1]

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b[0:2]
b[-1]
b[1, 2]
b[0:2, 2]

for row in b:
    print(row)

for cell in b.flat:
    print(cell)

c = np.arange(6)

c = np.arange(30).reshape(2,15)
c

np.hsplit(a,3)

