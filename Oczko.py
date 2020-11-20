import random
from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax

# Game rules: https://pl.wikipedia.org/wiki/Oczko_(gra_karciana)
# Authors: Gracjan Redwanc s17393, Dawid Szabłowski s16667
# Environment: Install easyAI - pip install easyAI


class Oczko(TwoPlayersGame):

    def __init__(self, players):
        """Initiates variables for game

            self.player - list of players
            self.pile - pile of cards
            self.nplayer - who starts the game first
            self.player1_score - score for Player
            self.player2_score - score for AI
            self.nplayer1_draw - currently drew card for Player
            self.nplayer2_draw - currently drew card for AI
            self.round_play - current round
            self.player1_moves - available moves for Player
            self.player2_moves - available moves for AI
        """
        self.players = players
        self.pile = [0, 0, 0, 0, 10, 10, 10, 10, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 11, 11, 11, 11]
        self.nplayer = 1
        self.player1_score = 0
        self.player2_score = 0
        self.nplayer1_draw = 0
        self.nplayer2_draw = 0
        self.round_play = 0
        self.player1_moves = ['1', '0']
        self.player2_moves = ['1', '0']

    def possible_moves(self):
        """Defines possible moves for AI and player

            Returns:
            list of "1" and "0"
            or
            String "0"
            Depending on previous moves made by player or AI
        """
        self.round_play = self.nmove
        if self.nplayer == 1:
            if self.player1_moves == ['1', '0']:
                return self.player1_moves
            else:
                return '0'
        elif self.nplayer == 2:
            if self.player2_moves == ['1', '0']:
                return self.player2_moves
            else:
                return '0'

    def make_move(self, move):
        """Defines how moves will influence the game

            If Player or AI picked '0' as their move they won't draw a new card,
            they won't be able to pick '1' anymore and their score will be returned.
            If Player or AI picked '1' they will draw a random card from card pile,
            that card pile will remove from itself drew card and the points from that
            card will be added to Player or AI score.
        """
        if self.nplayer == 1:
            if move == '0' and self.player1_moves == ['1', '0']:
                self.player1_moves.remove('1')
                return self.player1_score
            elif move == '1':
                draw = random.choice(self.pile)
                self.nplayer1_draw = draw
                self.pile.remove(draw)
                self.player1_score += draw

        if self.nplayer == 2:
            if move == '0' and self.player2_moves == ['1', '0']:
                self.player2_moves.remove('1')
                return self.player2_score
            elif move == '1':
                draw = random.choice(self.pile)
                self.nplayer2_draw = draw
                self.pile.remove(draw)
                self.player2_score += draw

    def lose(self, move):
        """Defines losing condition for AI

            Return:
            returns player score if conditions were met
        """
        if self.round_play == 3 and self.player1_score == 22:
            return self.player1_score

        if self.player1_score == 21 or (self.player2_score > 21 and self.round_play > 4):
            return self.player1_score

        if self.player2_score == 0 and move == ['0']:
            return self.player1_score

        if self.player1_score > self.player2_score and move == ['0']:
            return self.player1_score

    def win(self):
        """Defines winning condition for AI

            Return:
            returns AI score if conditions were met
        """
        if self.round_play == 4 and self.player2_score == 22:
            return self.player2_score

        if self.player2_score == 21 or (self.player1_score > 21 and self.round_play > 4):
            return self.player2_score

        if self.player2_score > self.player1_score and self.player1_moves == ['0']:
            return self.player2_score

        if self.round_play == 4 and self.player2_score == 22:
            return self.player2_score

    def is_over(self):
        """Defines when the game ends

            Returns:
            self.lose() if AI lost
            or
            self.win() if Player won
            Depending on which one is true
        """
        return self.lose(move='0') or self.win()

    def show(self):
        """Displays information about game

        """
        print("PLAYER DRAWS", self.nplayer1_draw)
        print("PLAYER SCORE", self.player1_score)
        print("AI DRAWS", self.nplayer2_draw)
        print("AI SCORE", self.player2_score)
        print(self.pile, "cards left in the pile")
        if self.lose(move='0'):
            print("PLAYER WON")
        elif self.win():
            print("AI WON")

    def scoring(self):
        """Defines scoring for AI depending on result of game

            Return:
            return -100 if AI loses
            else
            return 0
        """
        if self.lose(move='0'):
            return -100
        else:
            return 0


ai = Negamax(13)
game = Oczko([Human_Player(), AI_Player(ai)])
history = game.play()
