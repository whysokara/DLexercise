def fx(x):
  return 3*x**2 - 3*x + 4

# derivative function

def deriv(x):
  return 6*x - 3

# plot the function and its derivative

# defining range for x
x = np.linspace(-2,2,2001)

plt.plot(x,fx(x), x,deriv(x))
plt.xlim(x[[0,-1]])
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['y', 'dy'])
plt.show()

# Algorithm implementation

localmin = np.random.choice(x,1) # random starting point
# print(localmin)

# learning parameter
learning_rate = 0.01
training_epochs = 100

# run through training

for i in range(training_epochs):
  grad = deriv(localmin)
  localmin = localmin - learning_rate * grad
# print(localmin)

# plot the results
plt.plot(x, fx(x), x,deriv(x))
plt.plot(localmin,deriv(localmin),'ro')
plt.plot(localmin,fx(localmin),'ro')

plt.xlim(x[[0,-1]])
plt.grid()