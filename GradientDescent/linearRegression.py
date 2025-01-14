
import numpy as np
import matplotlib.pyplot as plt

# housing price dataset
X = np.array([500, 750, 1000, 1250, 1500])
Y = np.array([50, 75, 100, 125, 150])

# Normalize Data (Optional for better convergence)
X = (X - np.mean(X)) / np.std(X)
Y = (Y - np.mean(Y)) / np.std(Y)

# initialising parameters
m = 0
b = 0
learning_rate = 0.01
epochs = 1000
n = len(X)

# Gradient Descent
for _ in range(epochs):
    Y_pred = m * X + b
    dm = (-2/n) * np.sum(X * (Y - Y_pred))
    db = (-2/n) * np.sum(Y - Y_pred)
    m -= learning_rate * dm
    b -= learning_rate * db

# Prediction
print(f"Optimized m (slope): {m}")
print(f"Optimized b (intercept): {b}")

# Plot results
plt.scatter(X, Y, color='blue', label='Data Points')
plt.plot(X, m * X + b, color='red', label='Regression Line')
plt.xlabel('Size (normalized)')
plt.ylabel('Price (normalized)')
plt.legend()
plt.show()

