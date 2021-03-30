import random
import math 


class Player:
    def __init__(self, letter):
        self.letter = letter

class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """This function selects a random spot on the board from the available moves."""

        # Selecting a random available spot on the board given a game state.
        available_moves = game.get_available_moves(game.board)
        rand_choice = random.choice([k for k in available_moves.keys()]) 
        if any([True if k == rand_choice else False for k,v in available_moves.items()]):
            move_coordinate = available_moves[rand_choice]
        return move_coordinate


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """This function takes the user's spot selection and returns the coordinates."""
        available_moves = game.get_available_moves(game.board)
        move_is_valid = False
        while not move_is_valid:
            try:
                print('\n')
                move = int(input(f'{self.letter}\'s turn. Make a move (0-8): '))
                if move not in available_moves:
                    raise ValueError
                move_is_valid = True
                move_coordinate = available_moves[move]
            except ValueError:
                print('Invalid selection. Please try another number (0-8): ')
        return move_coordinate
    
class AiPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """This function returns the AI player's move."""

        # Selecting a random spot on the board if all spaces are available.
        available_moves = game.get_available_moves(game.board)
        if len(available_moves) == 9:
            rand_choice = random.choice([k for k in available_moves.keys()])
            move_coordinate = available_moves[rand_choice] 
        else:
            # If board isn't empty, return optimal move for AI player via minimax.
            move_coordinate = self.minimax(game, self.letter)['position']
            
        return move_coordinate

    def minimax(self, game_state, current_move):
        """
        This function enables the AI player to simulate all possible
        game scenarios via the minimax algorithm and return the optimal next move
        for it to make in the real game. 
        """
        max_player = self.letter 
        previous_move = 'O' if current_move == 'X' else 'X'

        # If the previous move was a winner, return the score of the winning result. 
        if game_state.winner == previous_move:
            return {'position': None, 'score': 1 * (game_state.empty_square_count(game_state.board) + 1) if previous_move == max_player else -1 * (game_state.empty_square_count(game_state.board) + 1)}
        # If the board is full but no winners, return a score of 0. 
        elif game_state.empty_square_count(game_state.board) == '0':
            return {'position': None, 'score': 0}

        # Assigning how best score starts given whose turn it is (maximizer or minimizer's).
        if current_move == max_player:
            best_score = {'position': None, 'score': -math.inf} 
        else:
            best_score = {'position': None, 'score': math.inf} 

        # Makes all available moves alternating players with each move made.
        for key, move in game_state.get_available_moves(game_state.board).items():
            game_state.make_move(game_state.board, move, current_move)
            sim_score = self.minimax(game_state, previous_move)

            # If a winner/tie is returned, clear the board of the spot selected that achieved that result,
            # , reset the game's winner to None, and assign the current board position to the simulated 
            # score's position value.
            row, col = move
            game_state.board[row][col] = ''
            game_state.winner = None
            game_state.tie = None
            sim_score['position'] = move
            
            # Replace the current best_score if the simulated score is more optimal for the current player. 
            if current_move == max_player:
                if sim_score['score'] > best_score['score']:
                    best_score = sim_score
            else:
                if sim_score['score'] < best_score['score']:
                    best_score = sim_score

        return best_score 

