import numpy as np

a = np.array([1,2,3])

a[0]

a[1]

a = np.array([[1,2], [3,4]])
a.ndim

b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
b.itemsize

b.dtype

c = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]], dtype = np.float64)
c.itemsize

c.shape

np.zeros((2,3))

np.ones((2,3,4), dtype = np.int16)

l=range(10)
l[0]

c.shape
c.reshape

c.ndim

np.arange(1,4)
np.arange(10, 30, 5)
