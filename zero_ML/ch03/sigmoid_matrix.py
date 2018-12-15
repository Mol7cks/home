import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
  return 1/(1 + np.exp(-x))

#1層目
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1,0.2,0.3])
A1 = np.dot(X, W1) + B1

Z1 = sigmoid(A1)
print(A1)
print(Z1)

#2層目
W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])
print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

#3層目
W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2,W3) + B3
Z3 = sigmoid(A3)

#4層目
def identity_function(x):
    return x

print(Z3.shape)
W4 = np.array([0.1,0.2])
B4 = np.array([0.1])
A4 = np.dot(Z3,W4) + B4
Y = identity_function(A4)
print(W4.shape)
print(A4.shape)
print(Y.shape)
print(Y)
