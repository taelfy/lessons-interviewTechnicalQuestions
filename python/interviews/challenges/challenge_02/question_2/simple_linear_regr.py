import numpy as np
from simple_linear_regr_utils import generate_data, evaluate, save_model, plot_data
import matplotlib.pyplot as plt


class SimpleLinearRegression:
    def __init__(self, iterations=15000, lr=0.1):
        self.iterations = iterations  # number of iterations the fit method will be called
        self.lr = lr  # The learning rate
        self.losses = []  # A list to hold the history of the calculated losses
        self.W, self.b = None, None  # the slope and the intercept of the model

    def __loss(self, y, y_hat):
        """

        :param y: the actual output on the training set
        :param y_hat: the predicted output on the training set
        :return:
            loss: the sum of squared error

        """

        loss = np.sum((y - y_hat) ** 2)
        self.losses.append(loss)
        return loss

    def __init_weights(self, X):
        """

        :param X: The training set
        """
        weights = np.random.normal(size=X.shape[1] + 1)
        self.W = weights[:X.shape[1]].reshape(-1, X.shape[1])
        self.b = weights[-1]

    def __sgd(self, X, y, y_hat):
        """

        :param X: The training set
        :param y: The actual output on the training set
        :param y_hat: The predicted output on the training set
        :return:
            sets updated W and b to the instance Object (self)
        """

        # TODO: this weight is not setup to account for additional features
        dW = -(2 / len(y)) * np.sum(X * (y - y_hat))  # slope
        db = -(2 / len(y)) * np.sum(y - y_hat)  # intercept

        self.W = self.W - self.lr * dW
        self.b = self.b - self.lr * db

    def fit(self, X, y):
        """

        :param X: The training set
        :param y: The true output of the training set
        :return:
        """
        self.__init_weights(X)
        y_hat = self.predict(X)
        loss = self.__loss(y, y_hat)
        print(f"Initial Loss: {loss}")
        for i in range(self.iterations + 1):
            self.__sgd(X, y, y_hat)
            y_hat = self.predict(X)
            loss = self.__loss(y, y_hat)
            if not i % 100:
                print(f"Iteration {i}, Loss: {loss}")

    def predict(self, X):
        """

        :param X: The training dataset
        :return:
            y_hat: the predicted output
        """
        # TODO: calculate the predicted output y_hat. remember the function of a line is defined as y = WX + b
        y_hat = self.W * X + self.b
        return y_hat

    @staticmethod
    def plot_data(x_data: None, y_data: None):
        """
        Visualise the data for observation and understanding.

        :param x_data:
        :param y_data:
        :return:
        """
        plt.scatter(x_data, y_data)
        plt.show()


if __name__ == "__main__":
    X_train, y_train, X_test, y_test = generate_data()
    model = SimpleLinearRegression()
    # NOTE: Use to visualise data first.
    # plot_data(X_train, y_train)
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    # save_model(model=model, save_path='../question_3/utils/artifacts/regression_model_v1.json')
    evaluate(model, X_test, y_test, predicted)
