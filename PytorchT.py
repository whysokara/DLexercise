import numpy as np
import torch

tv = torch.tensor([[5,2,6]])
print(tv)
print(tv.T)

tvT = tv.T
print(tvT.T)
