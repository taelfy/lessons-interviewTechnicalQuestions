import json

import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


def generate_data():
    """
    Generates a random dataset from a normal distribution.

    Returns:
        diabetes_X_train: the training dataset
        diabetes_y_train: The output corresponding to the training set
        diabetes_X_test: the test dataset
        diabetes_y_test: The output corresponding to the test set

    """
    # Load the diabetes dataset
    diabetes_X, diabetes_y = load_diabetes(return_X_y=True)

    # Use only one feature
    diabetes_X = diabetes_X[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20].reshape(-1, 1)
    diabetes_y_test = diabetes_y[-20:].reshape(-1, 1)

    print(f"# Training Samples: {len(diabetes_X_train)}; # Test samples: {len(diabetes_X_test)};")
    return diabetes_X_train, diabetes_y_train, diabetes_X_test, diabetes_y_test


def evaluate(model, X, y, y_predicted):
    """ Calculates and prints evaluation metrics. """
    # The coefficients
    print(f"Slope: {model.W}; Intercept: {model.b}")
    # The mean squared error
    mse = mean_squared_error(y, y_predicted)
    print(f"Mean squared error: {mse:.2f}")
    # The coefficient of determination: 1 is perfect prediction
    r2 = r2_score(y, y_predicted)
    print(f"Coefficient of determination: {r2:.2f}")

    # Plot outputs
    plt.scatter(X, y, color="black")
    plt.plot(X, y_predicted, color="blue", linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()

    if r2 >= 0.4:
        print("****** Success ******")
    else:
        print("****** Failed ******")


def plot_data(x_data: None, y_data: None):
    """
    Visualise the data for observation and understanding.

    :param x_data:
    :param y_data:
    :return:
    """
    print('Plotting data.')
    plt.scatter(x_data, y_data)
    plt.show()


def save_model(model: object, save_path=''):
    print('Saving model')
    regression_model_dict = {'slope': model.W[0][0], 'intercept': model.b}
    with open(save_path, 'w') as _f:
        json.dump(regression_model_dict, _f)
