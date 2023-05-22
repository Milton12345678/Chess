
#import time



chess_map = {
    0: 'a', 1: 'b', 2: 'c', 3: 'd',
    4: 'e', 5: 'f', 6: 'g', 7: 'h'
}

# Dictionary som kartlägger kolumnindex till schackbokstäverna a-h

def to_chess_coordinate(row, col):
    return chess_map[col] + str(8 - row)
    # Returnerar schackkoordinat baserat på rad och kolumn genom att kombinera bokstaven från chess_map med radnumret

def to_index(chess_coord):
    col, row = chess_coord[0], chess_coord[1]
    return 8 - int(row), ord(col) - ord('a')
    # Konverterar schackkoordinater till rad- och kolumnindex
    # Extraherar bokstaven och siffran från schackkoordinaten
    # Omvandlar bokstaven till motsvarande kolumnindex genom att subtrahera den från 'a'
    # Subtraherar radnumret från 8 för att konvertera det till radindex (eftersom brädet är orienterat uppifrån och ned)



class Pieces:
    def __init__(self, symbol, player, board):
        self.symbol = symbol
        self.player = player
        self.board = board
        # Skapar en instans av Pieces med symbol, spelare och bräde som attribut

    def __str__(self):
        return self.symbol
        # Returnerar symbolen för en instans av Pieces

    def move(self, current_position, new_position):
        current_row, current_col = to_index(current_position)
        new_row, new_col = to_index(new_position)
        # Konverterar aktuell position och ny position från schackkoordinater till rad- och kolumnindex

        if self.is_legal_move(current_row, current_col, new_row, new_col):
            if self.is_path_clear(current_row, current_col, new_row, new_col):
                if self.cant_take_own_color(current_row, current_col, new_row, new_col):
                    self.board.board[new_row][new_col] = self.symbol
                    self.board.board[current_row][current_col] = '""'
                    # Flyttar pjäsen till den nya positionen och tar bort den från den gamla positionen på brädet

                    current_chess_coord = to_chess_coordinate(current_row, current_col)
                    new_chess_coord = to_chess_coordinate(new_row, new_col)
                    # Konverterar rad- och kolumnindex till schackkoordinater

                    print(f"{self.symbol} flyttades från {current_chess_coord} till {new_chess_coord}")
                    # Skriver ut information om pjäsens drag

                    # Kontrollera om motståndarens kung fortfarande är vid liv
                    opponent_color = "vit" if self.player == "svart" else "svart"
                    if not self.board.is_king_alive(opponent_color):
                        winner_color = self.player
                        print(f"{winner_color.capitalize()} vinner! Motståndarens kung är inte längre i spelet.")
                        # Skriver ut vinnarmeddelande om motståndarens kung inte längre är i spelet
                        # Avsluta spelet eller utför eventuella nödvändiga åtgärder
                else:
                    print(f"{self.symbol} kan inte ta sin egen färg")
                    # Skriver ut meddelande om att pjäsen inte kan ta pjäser av samma färg
            else:
                print(f"Det finns en pjäs i vägen för {self.symbol}")
                # Skriver ut meddelande om att det finns en pjäs i vägen för pjäsens drag
        else:
            print(f"Ogiltigt drag för {self.symbol}")
            # Skriver ut meddelande om att draget är ogiltigt för pjäsen

    def is_legal_move(self, current_row, current_col, new_row, new_col):
        return True
    # Returnerar alltid True
    # Måste implementeras för att specificera regler för en legal flytt för en specifik pjäs

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        return True
        # Returnerar alltid True
        # Måste implementeras för att kontrollera om det finns några hinder på vägen för en specifik pjäs

    def cant_take_own_color(self, current_row, current_col, new_row, new_col):
        destination_piece = self.board.board[new_row][new_col]
        # Hämtar pjäsen på den nya positionen på brädet

        if self.player == "vit" and destination_piece in ['♙', '♘', '♗', '♕', '♖', '♔']:
            return False
            # Om spelaren är "vit" och destination_piece är en av pjäserna ['♙', '♘', '♗', '♕', '♖', '♔'], returnera False
            # Pjäsen kan inte ta pjäser av samma färg

        elif self.player == "svart" and destination_piece in ['♟', '♜', '♞', '♝', '♛', '♚']:
            return False
            # Om spelaren är "svart" och destination_piece är en av pjäserna ['♟', '♜', '♞', '♝', '♛', '♚'], returnera False
            # Pjäsen kan inte ta pjäser av samma färg

        return True
        # Returnerar True om pjäsen kan ta pjäsen på destinationen
        # Returnerar False om pjäsen inte kan ta pjäsen på destinationen på grund av färgrestriktioner

class Rook(Pieces):
    
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        return current_row == new_row or current_col == new_col
        # Kontrollerar om draget är lagligt för en tornpjäs genom att jämföra rad- och kolumnindex

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        if current_row == new_row:
            for col in range(min(current_col, new_col) + 1, max(current_col, new_col)):
                if self.board.board[current_row][col] != '""':
                    return False
            return True
            # Kontrollerar om vägen är fri för en horisontell rörelse genom att iterera över kolumnindexen mellan start- och slutpositionen
            # Om någon av de mellanliggande positionerna inte är tom returneras False, annars True
        elif current_col == new_col:
            for row in range(min(current_row, new_row) + 1, max(current_row, new_row)):
                if self.board.board[row][current_col] != '""':
                    return False
            return True
            # Kontrollerar om vägen är fri

    
            

class Knight(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        dx = abs(current_col - new_col)
        dy = abs(current_row - new_row)
        # Beräknar skillnaden i kolumn- och radpositioner mellan den nuvarande positionen och den nya positionen

        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            return True
            # Returnerar True om skillnaden i kolumnposition är 1 och skillnaden i radposition är 2
            # eller om skillnaden i kolumnposition är 2 och skillnaden i radposition är 1
            # Detta innebär att draget är enligt hästens mönster
            # Hästen kan hoppa över hinder och göra "L"-formade drag

        else:
            return False
            # Returnerar False om draget inte följer hästens mönster


class Bishop(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if current_row == new_row and current_col == new_col:
            return False
            # Returnerar False om den nuvarande positionen är samma som den nya positionen
            # Det är inte tillåtet att göra ett ogiltigt drag till samma position

        elif abs(current_row - new_row) == abs(current_col - new_col):
            return True
            # Returnerar True om skillnaden i radposition och kolumnposition är samma (i absoluta termer)
            # Detta betyder att draget är diagonalt
            # Löparen kan röra sig längs diagonala linjer

        else:
            return False
            # Returnerar False om draget inte är diagonalt

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        row_step = 1 if new_row > current_row else -1
        col_step = 1 if new_col > current_col else -1
        # Beräknar steglängden för raderna och kolumnerna baserat på om den nya positionen är högre eller lägre än den nuvarande positionen

        row, col = current_row + row_step, current_col + col_step
        # Sätter startpositionen för att undersöka stigen

        while row != new_row and col != new_col:
            # Loopar tills vi når den nya positionen

            if self.board.board[row][col] != "":
                return False
                # Om det finns en pjäs på vägen, returnera False
                # Stigen är inte klar för löparen

            row += row_step
            col += col_step
            # Flyttar till nästa position längs stigen

        return True
        # Returnerar True om stigen är klar för löparen
        # Returnerar False om det finns en pjäs på vägen för löparen



class Queen(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if abs(current_row - new_row) == abs(current_col - new_col) or current_row == new_row and current_col != new_col or current_row != new_row and current_col == new_col:
            return True
            # Returnerar True om draget är antingen diagonalt, horisontellt eller vertikalt
            # Kontrollerar om skillnaden i radposition och kolumnposition är antingen samma i absoluta termer (diagonalt) eller om endast en av dem är samma (horisontellt eller vertikalt)

        else:
            return False
            # Returnerar False om draget inte är diagonalt, horisontellt eller vertikalt

    def is_path_clear(self, current_row, current_col, new_row, new_col):
        if current_row == new_row:
            step = 1 if new_col > current_col else -1
            # Bestämmer steglängden baserat på om den nya kolumnpositionen är högre eller lägre än den nuvarande kolumnpositionen

            for col in range(current_col + step, new_col, step):
                if self.board.board[current_row][col] != "":
                    return False
                    # Om det finns en pjäs på vägen, returnera False
                    

        elif current_col == new_col:
            step = 1 if new_row > current_row else -1
            # Bestämmer steglängden baserat på om den nya radpositionen är högre eller lägre än den nuvarande radpositionen

            for row in range(current_row + step, new_row, step):
                if self.board.board[row][current_col] != "":
                    return False
                    # Om det finns en pjäs på vägen, returnera False
                   

        else:
            row_step = 1 if new_row > current_row else -1
            col_step = 1 if new_col > current_col else -1
            # Bestämmer steglängden för raderna och kolumnerna baserat på om den nya positionen är högre eller lägre än den nuvarande positionen

            row, col = current_row + row_step, current_col + col_step
            # Sätter startpositionen för att undersöka stigen

            while row != new_row and col != new_col:
                # Loopar tills vi når den nya positionen

                if self.board.board[row][col] != "":
                    return False
                    # Om det finns en pjäs på vägen, returnera False
                    # Stigen är inte klar för damen

                row += row_step
                col += col_step
                # Flyttar till nästa position längs stigen

        return True
        # Returnerar True om stigen är klar för damen
        # Returnerar False om det finns en pjäs på vägen för damen

class King(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if abs(current_row - new_row) <= 1 and abs(current_col - new_col) <= 1:
            return True
            # Returnerar True om skillnaden i radposition och kolumnposition är högst 1 i absoluta termer
            # Detta innebär att draget är giltigt om det sker en positionsförändring på högst 1 rad och 1 kolumn

        else:
            return False
            # Returnerar False om skillnaden i radposition och kolumnposition är större än 1
            # Detta innebär att draget är ogiltigt om det sker en positionsförändring på mer än 1 rad eller 1 kolumn


class Pawn(Pieces):
    def is_legal_move(self, current_row, current_col, new_row, new_col):
        if current_col == new_col:
            # Om kolumnpositionen förblir densamma (ingen sidoförflyttning)
            if self.player == 'white':
                # Om spelaren är vit
                if new_row == current_row - 1 or (current_row == 6 and new_row == current_row - 2):
                    return True
                    # Returnera True om den nya radpositionen är en rad upp från den nuvarande radpositionen
                    # eller om den nuvarande radpositionen är 6 (startposition för vit bonde) och den nya radpositionen är två rader upp
                else:
                    return False
                    # Returnera False i alla andra fall (ogiltigt drag för vit bonde)
            elif self.player == 'black':
                # Om spelaren är svart
                if new_row == current_row + 1 or (current_row == 1 and new_row == current_row + 2):
                    return True
                    # Returnera True om den nya radpositionen är en rad ner från den nuvarande radpositionen
                    # eller om den nuvarande radpositionen är 1 (startposition för svart bonde) och den nya radpositionen är två rader ner
                else:
                    return False
                    # Returnera False i alla andra fall (ogiltigt drag för svart bonde)
        elif abs(current_col - new_col) == 1 and abs(current_row - new_row) == 1:
            # Om det sker en sidoförflyttning med en skillnad på en kolumn och en rad
            if self.player == 'white' and new_row == current_row - 1:
                return True
                # Returnera True om spelaren är vit och den nya radpositionen är en rad upp från den nuvarande radpositionen
            elif self.player == 'black' and new_row == current_row + 1:
                return True
                # Returnera True om spelaren är svart och den nya radpositionen är en rad ner från den nuvarande radpositionen
            else:
                return False
                # Returnera False i alla andra fall (ogiltigt drag för bonden)


    def is_path_clear(self, current_row, current_col, new_row, new_col):
        if current_col == new_col:
            # Om kolumnpositionen förblir densamma (ingen sidoförflyttning)
            if self.player == 'white':
                step = -1
                # Om spelaren är vit, gå uppåt (minska radindexet) i loopar
            elif self.player == 'black':
                step = 1
                # Om spelaren är svart, gå nedåt (öka radindexet) i loopar

            for row in range(current_row + step, new_row, step):
                # Loopa genom raderna mellan den nuvarande radpositionen (exklusive) och den nya radpositionen
                if self.board.board[row][current_col] != '"" ':
                    return False
                    # Om det finns en pjäs på någon av de mellanliggande raderna, returnera False (saknade bana)

        else:
            return False
            # Om det är en sidoförflyttning (kolumnpositionen förändras), returnera False (ogiltig rörelse)
        return True
        # Returnera True om banan är fri från hinder (ingen pjäs mellan den nuvarande och nya positionen)

            
        
    


class Board:
    def __init__(self):
        self.board = [['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],  # En tvådimensionell lista som representerar brädet
                      ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
                      ['"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" ', '"" '],
                      ['♙ ', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
                      ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']]

    def __str__(self):
        return '\n'.join(['\t'.join(sep) for sep in self.board])
        # Returnerar en strängrepresentation av brädet där varje rad separeras med en ny rad och element i raden separeras med en tabulator

    def is_king_alive(self, color):
        king_symbol = '♔' if color == 'white' else '♚'  # Bestämmer symbolen för kungen baserat på färgen
        for row in self.board:
            if king_symbol in row:  # Om kungens symbol finns i raden
                return True  # Returnera True (kungen är vid liv)
        return False  # Returnera False (kungen är inte vid liv)


class Player:
    def __init__(self, name, color):
        self.name = name  # Spelarens namn
        self.color = color  # Spelarens färg (vit eller svart)

        if self.color == 'white':
            # Skapar och tilldelar spelarens pjäser och bönder för färgen vit
            self.pieces = [Rook('♖', self.color), Knight('♘', self.color), Bishop('♗', self.color),
                           Queen('♕', self.color), King('♔', self.color), Bishop('♗', self.color),
                           Knight('♘', self.color), Rook('♖', self.color)]
            self.pawns = [Pawn('♙', self.color) for i in range(8)]
            self.position = {'♖':[(7, 0), (7, 7)], '♘':[(7, 1), (7, 6)], '♗':[(7, 2), (7, 5)],
                              '♕':[(7, 3)], '♔':[(7, 4)], '♙':[(6, i) for i in range(8)]}
            # Positionen för varje pjäs och bonde för spelaren (vit)

        elif self.color == 'black':
            # Skapar och tilldelar spelarens pjäser och bönder för färgen svart
            self.pieces = [Rook('♜', self.color), Knight('♞', self.color), Bishop('♝', self.color),
                           Queen('♛', self.color), King('♚', self.color), Bishop('♝', self.color),
                           Knight('♞', self.color), Rook('♜', self.color)]
            self.pawns = [Pawn('♙', self.color) for i in range(8)]
            self.position = {'♜' :[(0, 0), (0, 7)], '♞':[(0, 1), (0, 6)], '♝':[(0, 2), (0, 5)],
                              '♛':[(0, 3)], '♚':[(0, 4)], '♟':[(1, i) for i in range(8)]}
            # Positionen för varje pjäs och bonde för spelaren (svart)
            
            
    
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

           
pawnW.move(('d2'),('d4'))
pawnB.move(('a7'),('a5'))
rookW.move(('a1'),('a3'))
rookB.move(('a8'),('a6'))
knightW.move(('b1'),('c3'))
pawnB.move(('g7'),('g5'))
knightW.move(('c3'),('d5'))
bishopB.move(('f8'),('g7'))
knightW.move(('d5'),('f6'))


knightW.move(('f6'),('e8'))


print(board)