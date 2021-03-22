import random

class Player:
    def __init__(self, letter):
        self.letter = letter

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, board, available_moves):
        rand_choice = random.choice([k for k in available_moves.keys()]) #selecting random key
        if any([True if k == rand_choice else False for k,v in available_moves.items()]):
            move_coordinate = available_moves[rand_choice]
            del available_moves[rand_choice]
        return move_coordinate

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, board, available_moves):
        move_is_valid = False
        move = None
        while not move_is_valid:
            try:
                print('\n')
                move = int(input(f'{self.letter}\'s turn. Make a move (0-8): '))
                if move not in available_moves:
                    raise ValueError
                move_is_valid = True
                move_coordinate = available_moves[move]
                del available_moves[move]
            except ValueError:
                print('Invalid selection. Please try another number (0-8): ')
        return move_coordinate

