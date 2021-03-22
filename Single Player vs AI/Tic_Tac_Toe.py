from player import HumanPlayer, ComputerPlayer, AiPlayer
import time

class Tic_Tac_Toe:
    def __init__(self, HumanPlayer, OtherPlayer):
        self.HumanPlayer = HumanPlayer
        self.OtherPlayer = OtherPlayer
        self.board = [['' for j in range(3)] for i in range(3)]
        self.available_moves = self.get_available_moves(self.board)
        self.winner = None

    def print_board(self, board):
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
        available_moves = {}
        counter = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '':
                    available_moves[counter] = (i,j)
                    counter+=1
        return available_moves

    def make_move(self, board, move, whose_move):
        if isinstance(whose_move, str):
            row, col = move
            board[row][col] = whose_move
        else:
            row, col = move
            board[row][col] = whose_move.letter

    def empty_square_count(self, board):
        return len([(i,j) for j in range(len(board)) for i in range(len(board))])

    def check_for_winner(self, board, whose_move):
        #check rows
        for i in range(len(board)):
            if all(board[i][j] == whose_move.letter for j in range(3)):
                return 'Winner'
            
        #check cols
        for i in range(len(board)):
            if all(board[j][i] == whose_move.letter for j in range(3)):
                return 'Winner'

        #check diagnols
        if all([board[i][j] == whose_move.letter for i,j in [(0,0),(1,1),(2,2)]]):
            return 'Winner'
        if all([board[i][j] == whose_move.letter for i,j in [(0,2),(1,1),(2,0)]]):
            return 'Winner'
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '':
                    continue
                else:
                    return False
        return 'Tie'
    
    def play_game(self):
        winner_not_found = True
        whose_move = self.HumanPlayer
        while winner_not_found:
            time.sleep(.5)
            self.print_board(self.board)
            move = whose_move.get_move(self)
            self.make_move(self.board, move, whose_move)
            if self.check_for_winner(self.board, whose_move)=='Winner':
                self.print_board(self.board)
                print('\n')
                print(f'Player {whose_move.letter} wins!')
                self.winner = whose_move.letter
                winner_not_found = False
            elif self.check_for_winner(self.board, whose_move)=='Tie':
                self.print_board(self.board)
                print('It\'s a tie!')
                self.winner = whose_move.letter
                winner_not_found = False
            else:
                if whose_move == self.HumanPlayer:
                    whose_move = self.OtherPlayer
                else:
                    whose_move = self.HumanPlayer
            continue


if __name__ == '__main__':
    t = Tic_Tac_Toe(HumanPlayer('X'), AiPlayer('O'))
    t.play_game()