import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


class MyLogisticRegression:
    def __init__(self, learning_rate=0.01, max_iterations=100):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.weights = None
        self.bias = 0

    def cost_function(self, X, y):
        m = X.shape[0]

        h_x = sigmoid(np.dot(X, self.weights) + self.bias)
        cost_function = (-1 / m) * (y * np.log(h_x) + (1 - y) * np.log(1 - h_x))

        bias_derivative = (1 / m) * (h_x - y)
        theta_derivative = (1 / m) * np.dot(X.T, np.subtract(h_x, y))

        return cost_function, theta_derivative, bias_derivative

    def optimize(self, X, y):
        for i in range(self.max_iterations):
            cost_func, theta_derivative, bias_derivative = self.cost_function(X, y)
            self.bias -= self.learning_rate * bias_derivative
            self.weights -= self.learning_rate * theta_derivative

    def fit(self, X_train, y_train):
        if self.weights is None:
            self.weights = np.zeros((X_train.shape[1], 1))

        self.optimize(X_train, y_train)

    def predict(self, X):
        probability = self.predict_proba(X)
        return [1 if prob >= 0.5 else 0 for prob in probability]

    def predict_proba(self, X):
        return sigmoid(np.dot(X, self.weights) + self.bias)

