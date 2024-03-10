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