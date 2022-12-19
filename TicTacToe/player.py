import math
import random

class Player:
    def __init__(self,letter) :
        #letter is X or O
        self.letter=letter
        

    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_move())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter + '\'s Your turn. Input move (0-8): ')
            try:
                val=int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square=True   #if these are successful, then yay!
            except ValueError:
                print("Invalid square. Try again")
        
        return val

