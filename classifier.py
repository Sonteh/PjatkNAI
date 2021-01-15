# SVM - Classification of datasets
# Authors: Gracjan Redwanc(s17393), Dawid Szabłowski(s16667)
# Enviroment: 
# install numpy
# install scikit-learn

import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics


class Classifier():
    def prepare_SVM(self, X, y):
        """
        Method prepares dataset and prints its accuracy
        """
        # Splits data into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        # Create a svm Classifier    
        clf = svm.SVC(kernel='rbf').fit(X, y)
        # Train the model using training sets
        clf.fit(X_train, y_train)
        # Predicit the results for the test dataset
        y_pred = clf.predict(X_test)
        self.clf = clf
        
        print('Accuracy of the model: ', metrics.accuracy_score(y_test, y_pred))

    def predict_based_on_input(self, data):
        """
        Takes user input and using predict function from svm to calculate result

        Returns: int
        """
        return int(self.clf.predict([data])[0])