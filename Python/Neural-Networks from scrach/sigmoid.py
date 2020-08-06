import numpy as np
import matplotlib.pyplot as plt

input_ = np.linspace(-10,10,100)

def sigmoid(X):
  val = 1/(1+np.exp(-X))
  return val

output = sigmoid(input_)

plt.plot(input_, output)