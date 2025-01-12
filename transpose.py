import numpy as np
import torch

# print(torch.__version__)

# create a vector
nv = np.array([[2,3,4]])
print(nv),print(' ')

# transpose
print(nv.T),print(' ')

# transpose the transpose

nvT = nv.T
print(nvT.T)

nm = np.array([[7,2,6],[4,5,8]])
print(nm), print(' ')

#transpose
print(nm.T), print(' ')

# t-t
nmT = nm.T
print(nmT.T)