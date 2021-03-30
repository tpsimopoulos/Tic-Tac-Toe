from player import HumanPlayer, RandomPlayer, AiPlayer
import time

class Tic_Tac_Toe:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = [['' for j in range(3)] for i in range(3)]
        self.winner = None
        self.tie = None

    def print_board(self, board):
        """Prints a representation of the current board."""
        print('\n')
        print('-------------------')
        print('\n')
        for i in range(len(board)):
            if i != 0:
                print('-----------')
            for j in range(len(board)):
                if j == 1:
                    print(' | ' + str(board[i][j]), end =" ")
                elif j == 2:
                    print(' | ' + str(board[i][j]))
                else:
                    print(board[i][j], end =" ")
    

    def get_available_moves(self, board):
        """Returns all available moves on given board."""
        available_moves = {}
        counter = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '':
                    available_moves[counter] = (i,j)
                counter+=1
        return available_moves


    def return_current_player_letter(self, current_player):
         # If called from minimax.
        if isinstance(current_player, str): 
            pass
        else:
            # If called from actual gameplay.
            current_player = current_player.letter 
        return current_player

        
    def make_move(self, board, move, current_player):
        """Given a spot on the board and a player, makes a move for that player."""
        row, col = move

        # Returning the letter of the current player. 
        current_player = self.return_current_player_letter(current_player)

        if board[row][col] == '':
            board[row][col] = current_player
            # Checking for winner or tie after move is made. 
            self.check_for_winner(self.board, current_player)
            self.check_for_tie(self.board, current_player)
        else:
            return False


    def empty_square_count(self, board):
        """Returns all the empty spaces currently on the board."""
        return len([(i,j) for j in range(len(board)) for i in range(len(board)) if board[i][j]==''])


    def check_for_winner(self, board, current_player):
        """
        Checks the board for any winning combination. If winning combination is found,
        function assigns current_player as the winner.
        """

        # Check rows.
        for i in range(len(board)):
            if all(board[i][j] == current_player for j in range(3)):
                self.winner = current_player
                return True
            
        # Check columns.
        for i in range(len(board)):
            if all(board[j][i] == current_player for j in range(3)):
                self.winner = current_player
                return True

        # Check diagnols.
        if all([board[i][j] == current_player for i,j in [(0,0),(1,1),(2,2)]]):
            self.winner = current_player
            return True
        if all([board[i][j] == current_player for i,j in [(0,2),(1,1),(2,0)]]):
            self.winner = current_player
            return True
    

    def check_for_tie(self, board, current_player):
        """Checks the board for a tie."""
        
        # Check tie. 
        if all(True if board[i][j] != '' else False for i in range(len(board)) for j in range(len(board))):
            self.tie = True 
            return True
    

    def play_game(self):
        """This function serves as the main game loop."""
        current_player = self.player_1
        
        # Only prints board out before selection if it's HumanPlayer's turn
        if type(current_player).__name__ == 'HumanPlayer':
            self.print_board(self.board)
        
        while not self.winner and not self.tie:
            time.sleep(.5)

            # Gets the move of player whose turn it is.
            move = current_player.get_move(self) 

            # Executes move returned by the current player
            self.make_move(self.board, move, current_player)
            self.print_board(self.board)

            if self.winner:
                print(f'Player {self.winner} wins!')
            elif self.tie:
                print('It\'s a tie!')

            # If there is no winner or tie, switch whose turn it is.
            current_player = self.player_1 if current_player == self.player_2 else self.player_2


if __name__ == '__main__':
    t = Tic_Tac_Toe(AiPlayer('O'), RandomPlayer('X'))
    t.play_game()