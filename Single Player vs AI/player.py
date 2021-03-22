import random
import math 


class Player:
    def __init__(self, letter):
        self.letter = letter

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        rand_choice = random.choice([k for k in game.available_moves.keys()]) #selecting random key
        if any([True if k == rand_choice else False for k,v in game.available_moves.items()]):
            move_coordinate = game.available_moves[rand_choice]
            del game.available_moves[rand_choice]
        return move_coordinate

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move_is_valid = False
        move = None
        while not move_is_valid:
            try:
                print('\n')
                move = int(input(f'{self.letter}\'s turn. Make a move (0-8): '))
                if move not in game.available_moves:
                    raise ValueError
                move_is_valid = True
                move_coordinate = game.available_moves[move]
                del game.available_moves[move]
            except ValueError:
                print('Invalid selection. Please try another number (0-8): ')
        return move_coordinate

class AiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves) == 9:
            rand_choice = random.choice([k for k in game.available_moves.keys()])
            move_coordinate = game.available_moves[rand_choice]
            del game.available_moves[rand_choice]
        else:
            #get square from minimax
            move_coordinate = self.minimax(game, self.letter)['position']
        return move_coordinate

    def minimax(self, game, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        #check if previous move is winner
        if game.winner == other_player:
            return {'position': None,
                    'score': 1 * (game.empty_square_count() + 1) if other_player == maxplayer else -1 * (game.empty_square_count() + 1)}

        elif not game.empty_square_count(game.board):
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for key, possible_move in game.available_moves.items():
            game.make_move(game.board, possible_move, player)
            #simulate what game would look like after the move is made
            sim_score = self.minimax(game, other_player)
            game.board[idx] = possible_move
            row, col = possible_move
            #undo move
            game.board[row][col] = ''
            game.winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best 

