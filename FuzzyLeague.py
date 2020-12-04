# Problem: Based on the user KDA, game length and minion score i want to know which mark player should get
# Authors: Gracjan Redwanc s17393, Dawid Szabłowski s16667
# Environment: Make sure you have python3, python3-venv and updated version of pip
# py -m venv env
# env\Scripts\activate
# pip install numpy
# pip install -U scikit-fuzzy
# pip install scipy
# for Windows you might need to download custom SciPy module from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
# and install it using pip install <file-path>

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyLeague:

    def __init__(self):
        """
        Prepares objects to work with fuzzy.

        Return:
        none
        """
        self.__universe_variables()
        self.__membership_functions()
        self.__fuzzy_rules()
        self.__control_system()

    def __universe_variables(self):
        """
        Creates universe variables.

        Return:
        none
        """

        self.minions = ctrl.Antecedent(np.arange(0, 301, 1), 'minions')
        self.length = ctrl.Antecedent(np.arange(0, 61, 1), 'length')
        self.kda = ctrl.Antecedent(np.arange(0, 21, 1), 'kda')
        self.mark = ctrl.Consequent(np.arange(0, 11, 1), 'mark')

    def __membership_functions(self):
        """
        Prepares membership functions.

        Return:
        none
        """
        self.mark['D'] = fuzz.trimf(self.mark.universe, [0, 0, 3])
        self.mark['C'] = fuzz.trimf(self.mark.universe, [2, 3.5, 5])
        self.mark['B'] = fuzz.trimf(self.mark.universe, [4, 5, 6])
        self.mark['A'] = fuzz.trimf(self.mark.universe, [5, 6.5, 8])
        self.mark['S'] = fuzz.trimf(self.mark.universe, [7, 10, 10])

        self.minions['below_100'] = fuzz.trimf(self.minions.universe, [0, 50, 100])
        self.minions['below_200'] = fuzz.trimf(self.minions.universe, [90, 150, 200])
        self.minions['below_300'] = fuzz.trimf(self.minions.universe, [190, 250, 300])

        self.length['ff15'] = fuzz.trimf(self.length.universe, [0, 10, 15])
        self.length['gg'] = fuzz.trimf(self.length.universe, [15, 20, 25])
        self.length['ggwp'] = fuzz.trimf(self.length.universe, [20, 30, 40])
        self.length['ezgame'] = fuzz.trimf(self.length.universe, [35, 45, 60])

        self.kda['inter'] = fuzz.trimf(self.kda.universe, [0, 0.5, 1.7])
        self.kda['average'] = fuzz.trimf(self.kda.universe, [1.5, 3.5, 5.5])
        self.kda['faker'] = fuzz.trimf(self.kda.universe, [5, 10, 20])

    def __fuzzy_rules(self):
        """
        Prepares set of rules for fuzzy logic.

        Return:
        none
        """
        self.rule1 = ctrl.Rule(antecedent=(
                (self.minions['below_100'] & self.length['ff15'] & self.kda['inter']) |  # 1
                (self.minions['below_100'] & self.length['ezgame'] & self.kda['inter']) |  # 5
                (self.minions['below_100'] & self.length['ggwp'] & self.kda['inter']) |
                (self.minions['below_100'] & self.length['gg'] & self.kda['inter']) |  # 4
                (self.minions['below_100'] & self.length['ezgame'] & self.kda['average'])), consequent=self.mark['D'] # 10
        )

        self.rule2 = ctrl.Rule(antecedent=(
                (self.minions['below_100'] & self.length['gg'] & self.kda['average']) |  # 8
                (self.minions['below_100'] & self.length['ggwp'] & self.kda['average']) |
                (self.minions['below_200'] & self.length['gg'] & self.kda['inter']) |  # 23
                (self.minions['below_200'] & self.length['ggwp'] & self.kda['inter']) |
                (self.minions['below_200'] & self.length['ezgame'] & self.kda['inter']) |  # 25
                (self.minions['below_300'] & self.length['ezgame'] & self.kda['inter'])), consequent=self.mark['C']  # 26
        )
        self.rule3 = ctrl.Rule(antecedent=(
                (self.minions['below_300'] & self.length['gg'] & self.kda['inter']) |  # 16
                (self.minions['below_100'] & self.length['gg'] & self.kda['faker']) |  # 11
                (self.minions['below_100'] & self.length['ezgame'] & self.kda['faker']) |  # 9
                (self.minions['below_200'] & self.length['gg'] & self.kda['average']) |  # 24
                (self.minions['below_200'] & self.length['ff15'] & self.kda['inter']) |  # 6
                (self.minions['below_100'] & self.length['ff15'] & self.kda['average']) |  # 2
                (self.minions['below_200'] & self.length['ggwp'] & self.kda['average']) |
                (self.minions['below_300'] & self.length['ggwp'] & self.kda['inter']) |
                (self.minions['below_100'] & self.length['ggwp'] & self.kda['faker']) |
                (self.minions['below_300'] & self.length['ezgame'] & self.kda['average']) |  # 17
                (self.minions['below_200'] & self.length['ezgame'] & self.kda['faker']) |  # 18
                (self.minions['below_200'] & self.length['ezgame'] & self.kda['average'])), consequent=self.mark['B']    # 27
        )
        self.rule4 = ctrl.Rule(antecedent=(
                (self.minions['below_100'] & self.length['ff15'] & self.kda['faker']) |  # 3
                (self.minions['below_300'] & self.length['ff15'] & self.kda['inter']) |  # 7
                (self.minions['below_200'] & self.length['ff15'] & self.kda['average']) |  # 12
                (self.minions['below_200'] & self.length['ggwp'] & self.kda['faker']) |
                (self.minions['below_300'] & self.length['ggwp'] & self.kda['average']) |
                (self.minions['below_300'] & self.length['gg'] & self.kda['average']) |  # 20
                (self.minions['below_200'] & self.length['gg'] & self.kda['faker'])), consequent=self.mark['A']  # 19
        )
        self.rule5 = ctrl.Rule(antecedent=(
                (self.minions['below_200'] & self.length['ff15'] & self.kda['faker']) |  # 22
                (self.minions['below_300'] & self.length['ff15'] & self.kda['average']) |  # 21
                (self.minions['below_300'] & self.length['ff15'] & self.kda['faker']) |  # 13
                (self.minions['below_300'] & self.length['gg'] & self.kda['faker']) |
                (self.minions['below_300'] & self.length['ggwp'] & self.kda['faker']) |  # 14
                (self.minions['below_300'] & self.length['ezgame'] & self.kda['faker'])), consequent=self.mark['S']   # 15
        )

    def __control_system(self):
        """
        Control system applies set of rules.

        Return:
        none
        """
        rating_ctrl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3, self.rule4, self.rule5])
        self.__rating = ctrl.ControlSystemSimulation(rating_ctrl)

    def fuzzy_inputs(self, minions, length, kda):
        """
        Inputs to fuzzy logic.

        Return:
        none
        """
        self.__rating.input['minions'] = minions
        self.__rating.input['length'] = length
        self.__rating.input['kda'] = kda
        self.__rating.compute()

    def fuzzy_output(self):
        """
        Gives you view of your mark and returns mark value.

        Return:
        Which mark player got
        """
        self.mark.view(sim=self.__rating)
        return self.__rating.output['mark']


def main():
    """
    Takes user input, counts user KDA based on user inputs and send those values to fuzzy.

    Return:
    None
    """
    fuzzy_lol = FuzzyLeague()

    minions = int(input("What was your minion score: "))
    length = int(input("How long was the game (1-60 minutes): "))
    kills = int(input("Your kills: "))
    deaths = int(input("Your deaths: "))
    assists = int(input("Your assists: "))
    if deaths == 0:
        kda = kills + assists
    else:
        kda = (kills + assists) / deaths

    fuzzy_lol.fuzzy_inputs(minions, length, kda)
    fuzzy_lol_mark = fuzzy_lol.fuzzy_output()

    print("Your KDA in that match was ", round(kda, 1), " and you have got ", round(fuzzy_lol_mark, 1), " mark.")


if __name__ == '__main__':
    main()
