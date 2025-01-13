import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

z = [1,2,3]
# Softmax result

num = np.exp(z)
den = np.sum(np.exp(z))

sigma = num/den

print(sigma)
print(np.sum(sigma)) ## always sums to 1

## using tensor

softfun = nn.Softmax(dim=0)
## Applying data to function
sigmaT = softfun(torch.Tensor(z))
print(sigmaT)

plt.plot(sigma, sigmaT,'ko')
plt.xlabel('"Manual" softmax')
plt.ylabel('Pytorch nn.softmax')