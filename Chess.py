
#import time

chess_map = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd',
    4: 'e', 5: 'f', 6: 'g', 7: 'h'
}

def to_chess_coordinate(row, col):
    return chess_map[col] + str(8 - row)

def to_index(chess_coord):
    col, row = chess_coord[0], chess_coord[1]
    return 8 - int(row), ord(col) - ord('a')


class Pieces:
    def move(self, current_position, new_position):
        current_row, current_col = to_index(current_position)
        new_row, new_col = to_index(new_position)

        if self.is_legal_move(current_row, current_col, new_row, new_col):
            if self.is_path_clear(current_row, current_col, new_row, new_col):
                if self.cant_take_own_color(current_row, current_col, new_row, new_col):
                    self.board.board[new_row][new_col] = self.symbol
                    self.board.board[current_row][current_col] = '""'

                    current_chess_coord = to_chess_coordinate(current_row, current_col)
                    new_chess_coord = to_chess_coordinate(new_row, new_col)

                    print(f"{self.symbol} moved from {current_chess_coord} to {new_chess_coord}")

                    
                    opponent_color = "white" if self.player == "black" else "black"
                    if not self.board.is_king_alive(opponent_color):
                        winner_color = self.player
                        print(f"{winner_color.capitalize()} wins! The opponent's king is no longer in the game.")
                        
                else:
                    print(f"{self.symbol} cannot take its own color")
            else:
                print(f"There is a piece in the path for {self.symbol}")
        else:
            print(f"Invalid move for {self.symbol}")

    def is_legal_move(self, current_row, current_col, new_row, new_col):
        return True

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        return True 

    def cant_take_own_color(self, current_row, current_col, new_row, new_col):
        destination_piece = self.board.board[new_row][new_col]
        if self.player == "white" and destination_piece in ['♙', '♘', '♗', '♕', '♖', '♔']:
            return False
        elif self.player == "black" and destination_piece in ['♟', '♜', '♞', '♝', '♛', '♚']:
            return False
        return True


class Rook(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if current_row == new_row and current_col != new_col:
            return True
        elif current_row != new_row and current_col == new_col:
            return True
        else:
            return False

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        if current_row == new_row:
            step = 1 if new_col > current_col else -1
            for col in range(current_col + step, new_col, step):
                if self.board.board[current_row][col] != '"" ':
                    return False
        else:
            step = 1 if new_row > current_row else -1
            for row in range(current_row + step, new_row, step):
                if self.board.board[row][current_col] != '"" ':
                    return False 
        return True 
    
            

class Knight(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
  
        dx = abs(current_col - new_col)
        dy = abs(current_row - new_row)
        
       
        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            return True
        else:
            return False



class Bishop(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if current_row == new_row and current_col == new_col:
            return False
        elif abs(current_row - new_row) == abs(current_col - new_col):
            return True
        else:
            return False

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        row_step = 1 if new_row > current_row else -1
        col_step = 1 if new_col > current_col else -1

        row, col = current_row + row_step, current_col + col_step
        while row != new_row and col != new_col:
            if self.board.board[row][col] != '"" ':
                return False
            row += row_step
            col += col_step

        return True


class Queen(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if abs(current_row - new_row) == abs(current_col - new_col) or current_row == new_row and current_col != new_col or current_row != new_row and current_col == new_col:
            return True
        else:
            return False

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        if current_row == new_row:
            step = 1 if new_col > current_col else -1
            for col in range(current_col + step, new_col, step):
                if self.board.board[current_row][col] != '"" ':
                    return False
        elif current_col == new_col:
            step = 1 if new_row > current_row else -1
            for row in range(current_row + step, new_row, step):
                if self.board.board[row][current_col] != '"" ':
                    return False
        else:
            row_step = 1 if new_row > current_row else -1
            col_step = 1 if new_col > current_col else -1

            row, col = current_row + row_step, current_col + col_step
            while row != new_row and col != new_col:
                if self.board.board[row][col] != '"" ':
                    return False
                row += row_step
                col += col_step

        return True

class King(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if abs(current_row - new_row) <= 1 and abs(current_col - new_col) <= 1:
            return True
        else:
            return False


class Pawn(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if current_col == new_col:
            if self.player == 'white':
                if new_row == current_row - 1 or (current_row == 6 and new_row == current_row - 2):
                    return True
                else:
                    return False
            elif self.player == 'black':
                if new_row == current_row + 1 or (current_row == 1 and new_row == current_row + 2):
                    return True
                else:
                    return False
        elif abs(current_col - new_col) == 1 and abs(current_row - new_row) == 1:
            if self.player == 'white' and new_row == current_row - 1:
                return True
            elif self.player == 'black' and new_row == current_row + 1:
                return True
            else:
                return False


    def is_path_clear(self, current_row, current_col, new_row, new_col):
        if current_col == new_col:
            if self.player == 'white':
                step = -1
            elif self.player == 'black':
                step = 1

            
            for row in range(current_row + step, new_row, step):
                if self.board.board[row][current_col] != '"" ':
                    return False
        else:
            return False

        return True

            
        
    


class Board:
    def __init__(self):
        self.board = [['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
                      ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
                      ['"" '"", '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['"" '"", '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['"" '"", '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['"" '"", '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['♙ ', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
                      ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']]

    def __str__(self):
        return '\n'.join(['\t'.join(sep) for sep in self.board])
    def is_king_alive(self, color):
        king_symbol = '♔' if color == 'white' else '♚'
        for row in self.board:
            if king_symbol in row:
                return True
        return False
    

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        if self.color == 'white':
            self.pieces = [Rook('♖', self.color), Knight('♘', self.color), Bishop('♗', self.color),
                           Queen('♕', self.color), King('♔', self.color), Bishop('♗', self.color),
                           Knight('♘', self.color), Rook('♖', self.color)]
            self.pawns = [Pawn('♙', self.color) for i in range(8)]
            self.position = {'♖':[(7, 0), (7, 7)], '♘':[(7, 1), (7, 6)], '♗':[(7, 2), (7, 5)],
                              '♕':[(7, 3)], '♔':[(7, 4)], '♙':[(6, i) for i in range(8)]}
        elif self.color == 'black':
            self.pieces = [Rook('♜', self.color), Knight('♞', self.color), Bishop('♝', self.color), Queen('♛', self.color), King('♚', self.color), Bishop('♝', self.color),
                           Knight('♞', self.color), Rook('♜', self.color)]
            self.pawns = [Pawn('♙', self.color) for i in range(8)]
            self.position = {'♜' :[(0, 0), (0, 7)], '♞':[(0, 1), (0, 6)], '♝':[(0, 2), (0, 5)],
                              '♛':[(0, 3)], '♚':[(0, 4)], '♟':[(1, i) for i in range(8)]}
        
            
            
    
board = Board()
            
            
rookW = Rook('♖', 'white', board)
knightW = Knight('♘', 'white', board)
bishopW = Bishop('♗', 'white', board)
pawnW = Pawn('♙', 'white', board)
queenW = Queen('♕', 'white', board)
kingW = King('♔', 'white', board)
rookB = Rook('♜','black', board)
knightB = Knight('♞', 'black', board)
bishopB = Bishop('♝', 'black', board)
queenB = Queen('♛', 'black', board)
kingB = King('♚', 'black', board)
pawnB = Pawn('♟', 'black', board)
empty = Pieces('  ', None, board)    

           
pawnW.move(('d2'),('d3'))
bishopW.move(('c1'),('d2'))
pawnW.move(('a2'),('a3'))
bishopW.move(('d2'),('a5'))
pawnW.move(('a3'),('a4'))
pawnW.move(('a4'),('a6'))
rookW.move(('a1'),('a2'))
pawnW.move(('b2'),('b4'))
rookW.move(('a2'),('b2'))
rookW.move(('b2'),('b3'))
rookW.move(('b3'),('c3'))
rookW.move(('c3'),('c7'))
pawnW.move(('e2'),('e3'))
queenW.move(('d1'),('f3'))
print(board) 
