# SVM - Classification of datasets
# Authors: Gracjan Redwanc(s17393), Dawid Szabłowski(s16667)
# Enviroment: 
# install numpy
# install scikit-learn

import numpy as np
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from classifier import Classifier


def main():
    """
    App main method
    Allows user to chose which dataset he wants to use
    """
    print('Which dataset would you like to run?')
    choice_number = int(input("1 = Which type of Iris Flower, 2 = Lol whos side won, 10-min prediction: "))
    data = None
    classifier = Classifier()

    if choice_number == 1:
        iris_dataset = datasets.load_iris()
        classifier.prepare_SVM(iris_dataset.data, iris_dataset.target)
        data = get_iris_info()

        print('0 - setosa | 1 - versicolor | 2 - virginica')
        print('Predicted flower type: ', classifier.predict_based_on_input(data))
    elif choice_number == 2:
        data_file = open("./data/league_dataset.csv")
        lol_dataset = np.genfromtxt(fname = data_file, delimiter=";", dtype=None, encoding='UTF-8')

        X = lol_dataset[1:, :-1]
        y = lol_dataset[1:, -1]
        classifier.prepare_SVM(X, y)

        data = get_game_lol_info()
        print('0 - Red Win | 1 - Blue win ')
        print('Predicted side win: ', classifier.predict_based_on_input(data))
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

def get_game_lol_info():
    """
    Gets input from the user and returns array with data about match

    Returns: array
    """
    blue_wards = int(input("Wards placed by blue team: "))
    blue_firstblood = int(input("Firstblood by blue team 1-yes 0-no: "))
    blue_kills = int(input("Total kills made by blue team: "))
    blue_deaths = int(input("Total deaths of blue team: "))
    blue_assists = int(input("Total assists of blue team: "))
    blue_monsters = int(input("Epic monsters killed by blue team: "))
    blue_dragons = int(input("Dragons killed by blue team: "))
    blue_heralds = int(input("Heralds killed by blue team: "))
    blue_towers = int(input("Towers destroyed by blue team: "))
    blue_gold = int(input("Total gold of blue team: "))
    blue_level = float(input("Average level of blue team: "))
    blue_minions = int(input("Total minions killed by blue team: "))
    red_wards = int(input("Wards placed by red team: "))
    red_firstblood = int(input("Firstblood by red team 1-yes 0-no: "))
    red_kills = int(input("Total kills made by red team: "))
    red_deaths = int(input("Total deaths of red team: "))
    red_assists = int(input("Total assists of red team: "))
    red_monsters = int(input("Epic monsters killed by red team: "))
    red_dragons = int(input("Dragons killed by red team: "))
    red_heralds = int(input("Heralds killed by red team: "))
    red_towers = int(input("Towers destroyed by red team: "))
    red_gold = int(input("Total gold of red team: "))
    red_level = float(input("Average level of red team: "))
    red_minions = int(input("Total minions killed by red team: "))
    
    blue_gold_diff = blue_gold - red_gold
    red_gold_diff = red_gold - blue_gold

    return np.array([blue_wards, blue_firstblood, blue_kills, blue_deaths, blue_assists, blue_monsters, blue_dragons, blue_heralds, blue_towers, blue_gold, blue_level,
                    blue_minions, blue_gold_diff, red_wards, red_firstblood, red_kills, red_deaths, red_assists, red_monsters, red_dragons, red_heralds, red_towers,
                    red_gold, red_level, red_minions, red_gold_diff])

if __name__ == "__main__":
    main()