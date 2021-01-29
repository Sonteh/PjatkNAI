# SVM - Classification of datasets
# Authors: Gracjan Redwanc(s17393), Dawid Szabłowski(s16667)
# Enviroment: 
# install numpy
# install scikit-learn

import numpy as np
from sklearn import datasets
from iris_flower_neural_network import Neural_Network


def main():
    """
    App main method
    Allows user to chose which dataset he wants to use
    """
    print('Which dataset would you like to run?')
    choice_number = int(input("1 = Which type of Iris Flower, 2 = Lol whos side won, 10-min prediction: "))
    data = None
    neural_network = Neural_Network()

    if choice_number == 1:
        iris_dataset = datasets.load_iris()
        neural_network.prepare_neural_network(iris_dataset.data, iris_dataset.target)
        data = get_iris_info()

        print('0 - setosa | 1 - versicolor | 2 - virginica')
        print('Predicted flower type: ', neural_network.predict_based_on_input(data))
    elif choice_number == 2:
        return true
    else:
        raise ValueError("You picked wrong number.")

    

def get_iris_info():
    """
    Gets input from the user and returns array with data about iris

    Returns: array
    """
    sepal_length = float(input("Sepal length in cm: "))
    sepal_width = float(input("Sepal width in cm: "))
    petal_length = float(input("Petal length in cm: "))
    petal_width = float(input("Petal width in cm: "))

    return np.array([sepal_length, sepal_width, petal_length, petal_width])


if __name__ == "__main__":
    main()