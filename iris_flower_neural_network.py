import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

class Neural_Network():
    def prepare_neural_network(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)
        print(X_train.shape); print(X_test.shape)

        mlp = MLPClassifier(hidden_layer_sizes=(4,4,4), activation='relu', solver='adam', max_iter=2500)
        mlp.learning_rate_init = 0.005
        mlp.fit(X_train, y_train)

        predict_train = mlp.predict(X_train)
        predict_test = mlp.predict(X_test)

        print(confusion_matrix(y_train, predict_train))
        print(classification_report(y_train, predict_train))

        print(confusion_matrix(y_test, predict_test))
        print(classification_report(y_test, predict_test))

        self.mlp = mlp

    def predict_based_on_input(self, data):
        return int(self.mlp.predict([data]))