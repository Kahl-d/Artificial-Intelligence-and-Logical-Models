import math
from math import sin, pi
from random import random
import matplotlib.pyplot as plt


def f(x):
    return sin(pi * x)


def generate_training_examples(n=2):
    xs = [random() * 2 - 1 for _ in range(n)]
    return [(x, f(x)) for x in xs]


def fit_without_reg(examples):
    """Computes values of w0 and w1 that minimize the sum-of-squared-errors cost function

    Args:
    - examples: a list of two (x, y) tuples, where x is the feature and y is the label
    """
    w0 = 0
    w1 = 0
    ## BEGIN YOUR CODE ##

    x1, y1 = examples[0]
    x2, y2 = examples[1]

    #Calculate w1 (slope)
    w1 = (y2 - y1) / (x2 - x1)

    # Calculate w0 (intercept)
    w0 = y1 - w1 * x1

    ## END YOUR CODE ##
    return w0, w1


def fit_with_reg(examples, lambda_hp):
    """Computes values of w0 and w1 that minimize the regularized sum-of-squared-errors cost function

    Args:
    - examples: a list of two (x, y) tuples, where x is the feature and y is the label
    - lambda_hp: a float representing the value of the lambda hyperparameter; a larger value means more regularization
    """
    w0 = 0
    w1 = 0
    ## BEGIN YOUR CODE ##

    x1, y1 = examples[0]
    x2, y2 = examples[1]

     # Using gradient descent
    n = 0.05
    for i in range(1000):
        # Compute the gradients
        dw0 = 2 * w0 * (2 + lambda_hp) + 2 * w1 * (x1 + x2) - 2 * (y1 + y2)
        dw1 = 2 * w0 * (x1 + x2) + 2 * w1 * (x1**2 + x2**2 + lambda_hp) - 2 * (x1 * y1 + x2 * y2)

        # Update the weights
        w0 = w0 - n * dw0
        w1 = w1 - n * dw1


    ## END YOUR CODE ##
    return (w0, w1)


def test_error(w0, w1):
    n = 100
    xs = [i/n for i in range(-n, n + 1)]
    return sum((w0 + w1 * x - f(x)) ** 2 for x in xs) / len(xs)

# Function to plot the lines given the pairs of w0 and w1
def plot_lines(pairs, title):
    # Set up the plot
    plt.figure(figsize=(7, 7))
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-5, 5)

    for w0, w1 in pairs:
        # Plot the line
        xs = [-1, 1]
        ys = [w0 + w1 * x for x in xs]
        plt.plot(xs, ys, color='blue', alpha=0.05)

    # Plot the target function f(x)
    x_vals = [i / 100.0 for i in range(-100, 101)]
    y_vals = [f(x) for x in x_vals]
    plt.plot(x_vals, y_vals, color='red')

    plt.show()


if __name__ == "__main__":

    error_without_reg = 0
    error_with_reg = 0

    without_reg_pairs = []
    with_reg_pairs = []

    for i in range(1000):
        examples = generate_training_examples()
        w0, w1 = fit_without_reg(examples)
        error_without_reg += test_error(w0, w1)
        without_reg_pairs.append((w0, w1))
        
        w0, w1 = fit_with_reg(examples, 1)
        error_with_reg += test_error(w0, w1)
        with_reg_pairs.append((w0, w1))

    print("Average test error without regularization:", error_without_reg / 1000)
    print("Average test error with regularization:", error_with_reg / 1000)

    plot_lines(without_reg_pairs, "Without Regularization")
    plot_lines(with_reg_pairs, "With Regularization")