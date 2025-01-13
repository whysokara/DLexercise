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