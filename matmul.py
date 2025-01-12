import numpy as np
import torch

A = np.random.randn(3, 4)
B = np.random.randn(4, 5)
C = np.random.randn(3, 7)

# print(np.round(A@B, 2))
# print(np.round(A@C, 2))
print(np.round(C.T@A, 2)), print(' ')


# with pytorch, just use torch.random