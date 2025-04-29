import numpy as np

class TicTacToe:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 pour X, 2 pour O
        self.game_over = False
        self.winner = None
        self.winning_line = None
    
    def make_move(self, row, col):
        if self.game_over or not (0 <= row < 3) or not (0 <= col < 3):
            return False
        
        if self.board[row][col] != 0:
            return False
        
        self.board[row][col] = self.current_player
        
        if self.check_winner(row, col):
            self.game_over = True
            self.winner = self.current_player
        elif np.all(self.board != 0):
            self.game_over = True
        
        self.current_player = 3 - self.current_player  # Alterne entre 1 et 2
        return True
    
    def check_winner(self, row, col):
        player = self.board[row][col]
        
        # Vérification ligne
        if np.all(self.board[row] == player):
            self.winning_line = ('row', row)
            return True
        
        # Vérification colonne
        if np.all(self.board[:, col] == player):
            self.winning_line = ('col', col)
            return True
        
        # Vérification diagonales
        if row == col and np.all(np.diag(self.board) == player):
            self.winning_line = ('diag', 1)
            return True
        
        if row + col == 2 and np.all(np.diag(np.fliplr(self.board)) == player):
            self.winning_line = ('diag', 2)
            return True
        
        return False
    
    def get_valid_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    moves.append((i, j))
        return moves
    
    def get_state(self):
        return {
            'board': self.board.copy(),
            'current_player': self.current_player,
            'game_over': self.game_over,
            'winner': self.winner,
            'winning_line': self.winning_line
        }