import numpy as np

a = np.arange(12).reshape(3,4)
a

for cell in a.flatten():
    print(cell)

for x in np.nditer(a, order = 'F', flags = ['external_loop']):
    print(x)

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x

b = np.arange(3,15, 4).reshape(3,1)
b

for x,y in np.nditer([a,b]):
    print(x,y)