# Description: This file contains the implementation of the Stochastic Gradient Descent algorithm.
import numpy as np


# Data
# Xi
X = np.array([-5, 1, -2, 2, 4, 7]) 
# yi
y = np.array([-1, 1, -1, -1, 1, 1])

# Initialize weights
w_1 = 0.0  
w_0 = 0.0  

# Learning Rate
learning_rate = 0.01 
convergence_threshold = 1e-6  
max_iterations = 1000

# Cost Function: Hinge Loss
# This function calculates the hinge loss for the given data and weights
def hinge_loss(X, y, w_1, w_0):
    hinge_losses = np.maximum(0, 1 - y * (X * w_1 + w_0))
    return np.sum(hinge_losses)


# Gradient Descent
# This function implements the stochastic gradient descent algorithm
# It updates the weights w_1 and w_0 using the hinge loss and its gradients
# The algorithm stops when the loss is less than the convergence threshold
# or the maximum number of iterations is reached

def gradient_descent(X, y, w_1, w_0, learning_rate, convergence_threshold, max_iterations):

    for i in range(max_iterations):

        predictions = w_1 * X + w_0

        indicator = (1 - y * predictions) > 0

        dw = np.mean(-X * y * indicator)
        db = np.mean(-y * indicator)

        w_1 -= learning_rate * dw
        w_0 -= learning_rate * db

        loss = hinge_loss(X, y, w_1, w_0)


        if loss < convergence_threshold:
            break


    return w_1, w_0



w_1, w_0 = gradient_descent(X, y, w_1, w_0, learning_rate, convergence_threshold, max_iterations)

# Print the converged weights
print(f"Converged weights: w1=: {w_1}, w0: {w_0}")

## Comarison with part c
# results from part c
# w_0 = -0.1 w_1 = 0.4

# Results from SGD
# w_0 = -0.3333 w_1 = 0.340000

# We can seee that the w_1 is almomst same for the two methods but w_0 is different.

