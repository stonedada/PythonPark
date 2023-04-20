import random

import numpy as np

a=np.random.random((2,2))
b = np.array([[1, 2], [3, 4]])
c = np.array([[5, 5], [5, 6]])
print(b, '\n', c)

e=b[c == 5]
print(type(e))
print(e.shape)
# f=(a>0)
# print(f)
