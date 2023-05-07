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
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if current_col == new_col:  
            if self.player == 'white':
                if new_row == current_row - 1:
                    return True
                else:
                    return False
            elif self.player == 'black':
                if new_row == current_row + 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


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
rookW1 = Rook('♖', 'white')
rookW2 = Rook('♖', 'white')
knightW1 = Knight('♘', 'white')
knightW2 = Knight('♘', 'white')
bishopW1 = Bishop('♗', 'white')
bishopW2 = Bishop('♗', 'white')
pawnW1 = Pawn('♙', 'white')
pawnW2 = Pawn('♙', 'white')
pawnW3 = Pawn('♙', 'white')
pawnW4 = Pawn('♙', 'white')
pawnW5 = Pawn('♙', 'white')
pawnW6 = Pawn('♙', 'white')
pawnW7 = Pawn('♙', 'white')
pawnW8 = Pawn('♙', 'white')
queenW = Queen('♕', 'white')
kingW = King('♔', 'white')
rookB1 = Rook('♜', 'black')
rookB2 = Rook('♜', 'black')
knightB1 = Knight('♞', 'black')
knightB2 = Knight('♞', 'black')
bishopB1 = Bishop('♝', 'black')
bishopB2 = Bishop('♝', 'black')
queenB = Queen('♛', 'black')
kingB = King('♚', 'black')
pawnB1 = Pawn('♟', 'black')
pawnB2 = Pawn('+', 'black')
pawnB3 = Pawn('♟', 'black')
pawnB4 = Pawn('♟', 'black')
pawnB5 = Pawn('♟', 'black')
pawnB6 = Pawn('♟', 'black')
pawnB7 = Pawn('♟', 'black')
pawnB8 = Pawn('♟', 'black')
empty = Pieces('  ', None)  
           
            #Rs Cs   R   C
            

pawnB1.move((1,0), (2,0))
print(board)