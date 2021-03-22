class Tic_Tac_Toe:
    def __init__(self):
        self.player1 = ''
        while self.player1 != 'X' and self.player1 != 'O':
            self.player1 = input('Player 1, choose X or O: ').upper()
        if self.player1 == 'X':
            self.player2 = 'O'
        else: 
            self.player2 = 'X'
        self.board = [['' for j in range(3)] for i in range(3)]
        print(f'Player 1 is {self.player1}')
        print(f'Player 2 is {self.player2}')

    def print_board(self, board):
        for i in range(len(board)):
            if i != 0:
                print('---------')
            for j in range(len(board)):
                if j == 1:
                    print(' | ' + str(board[i][j]), end =" ")
                elif j == 2:
                    print(' | ' + str(board[i][j]))
                else:
                    print(board[i][j], end =" ")
    
    def get_move(self, whose_move):
        move = input(f'Player {whose_move}, make your move (in x,y form). ')
        return tuple(int(i) for i in move.split(','))

    def is_valid_move(self, board, move, whose_move):
        try:
            row, col = move
            if board[row][col] == '':
                board[row][col] = whose_move
                return True
            else:
                print('ERROR: Spot already taken. Please select a different spot.')
                return False
        except IndexError:
            print(f'ERROR: Player {whose_move}, the spot you\'ve selected isn\'t a valid spot. Please try again.')
            return False
        except ValueError:
            print(f'ERROR: Player {whose_move}, please input your spot selection in x,y form.')
            return False
        
    def check_for_winner(self, board, whose_move):
        #check rows
        for i in range(len(board)):
            if board[i][0] == whose_move and board[i][1] == whose_move and board[i][2] == whose_move:
                return 'Winner'
            
        #check cols
        for i in range(len(board)):
            if board[0][i] == whose_move and board[1][i] == whose_move and board[2][i] == whose_move:
                return 'Winner'
    
        #check diagnols
        if board[0][0] == whose_move and board[1][1] == whose_move and board[2][2] == whose_move:
            return 'Winner'
        elif board[0][2] == whose_move and  board[1][1] == whose_move and board[2][0] == whose_move:
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
        whose_move = self.player1
        while winner_not_found:
            self.print_board(self.board)
            move = self.get_move(whose_move)
            if self.is_valid_move(self.board, move, whose_move):
                if self.check_for_winner(self.board, whose_move)=='Winner':
                    self.print_board(self.board)
                    print(f'Player {whose_move} wins!"')
                    winner_not_found = False
                if self.check_for_winner(self.board, whose_move)=='Tie':
                    self.print_board(self.board)
                    print('It\'s a tie!')
                    winner_not_found = False
                else:
                    if whose_move == self.player1:
                        whose_move = self.player2
                    else:
                        whose_move = self.player1
            else:
                continue