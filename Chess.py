class Pieces:
    def __init__(self, symbol, player):
        self.symbol = symbol
        self.player = player
    
    def __str__(self):
        return self.symbol

    def move(self, current_position, new_position):
        #definerar den nuvariga raden och columen med hjälp av olika index
        current_row, current_col = current_position[0], current_position[1]

        #gör samma sak fast för den nya posistionen för raden och columnen
        new_row, new_col = new_position[0], new_position[1]

        # Checkar om draget är lagligt 
        if self.is_legal_move(current_row, current_col, new_row, new_col):
            #upptaterar brädet med den nya posistionen
            board.board[new_row][new_col] = self.symbol
            board.board[current_row][current_col] = '  '
            return f"{self.symbol} moved from {current_position} to {new_position}"
        else:
            return f"Invalid move for {self.symbol}"

    def is_legal_move(self, current_row, current_col, new_row, new_col):
     #lägger till en code som tittar om draget är "valid" för enkelhetens skull så returnar den alltid true
        return True


class Rook(Pieces):
    pass


class Knight(Pieces):
    pass


class Bishop(Pieces):
    pass


class Queen(Pieces):
    pass


class King(Pieces):
    pass


class Pawn(Pieces):
    pass


class Board:
    def __init__(self):
        self.board = [['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
                      ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                      ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
                      ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']]
#Funktion som separerar rader 
    def __str__(self):
        return '\n'.join(['\t'.join(sep) for sep in self.board])


# 'W' innan står för White och 'B' innan står för black 
Player1.white = ("white","W")
Player2.black = ("black", "B")

board = Board()
rookW = Rook('♖')
rookW = Rook('♖')
knightW = Knight('♘')
knightW = Knight('♘')
bishopW = Bishop('♗')
bishopW = Bishop('♗')
pawnW = Pawn('♙')
pawnW = Pawn('♙')
pawnW = Pawn('♙')
pawnW = Pawn('♙')
pawnW = Pawn('♙')
pawnW = Pawn('♙')
pawnW = Pawn('♙')
pawnW = Pawn('♙')
queenW = Queen('♕')
kingW = King('♔')
rookB = Rook('♜')
rookB = Rook('♜')
knightB = Knight('♞')
knightB = Knight('♞')
bishopB = Bishop('♝')
bishopB = Bishop('♝')
queenB = Queen('♛')
kingB = King('♚')
pawnB = Pawn('♟')
pawnB = Pawn('♟')
pawnB = Pawn('♟')
pawnB = Pawn('♟')
pawnB = Pawn('♟')
pawnB = Pawn('♟')
pawnB = Pawn('♟')
pawnB = Pawn('♟')
empty = Pieces('  ')
            #Rs Cs   R   C
pawnB.move((1, 1), (2, 1))
print(board)