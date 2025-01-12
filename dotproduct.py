import numpy as np
import torch

nv1 = np.array([2,3,4])
nv2 = np.array([1,0,-2])

print(np.dot(nv1,nv2))
print(sum(nv1*nv2))

## in tensors

nv1 = torch.tensor([2,3,4])
nv2 = torch.tensor([1,0,-2])

print(torch.dot(nv1,nv2))
print(torch.sum(nv1*nv2))