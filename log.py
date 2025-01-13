import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(.001, 1, 200) # generating 200 random numbers between .001 and 1
logx = np.log(x)

# plot

fig = plt.figure(figsize=(10, 4))
plt.plot(x, logx, 'ks-', markerfacecolor='w')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.show()