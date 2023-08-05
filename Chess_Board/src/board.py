from const import *
from square import Square
from piece import *
from move import Move
class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_piece('white')
        self._add_piece('black')
        
    def calc_moves(self, piece, row, col):
        '''
        calculate  all the possible (valid) moves of an specific piece on a specific position 
        '''
        def pawn_moves():
            steps = 1 if piece.moved else 2
            
            # vartical moves
            start = row + piece.dir
            end  = row + (piece.dir *(1 + steps))
            
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # create intial and final move
                        initial =  Square(row, col)
                        final  = Square(possible_move_row, col)
                        
                        # create a new moves
                        move = Move(initial, final)
                        # append new move
                        piece.add_move(move)
                    # blocked
                    else: break
                    # not in range
                else: break
            
            # diagonal moves
            possible_move_row  = row +piece.dir
            possible_move_cols = [col -1, col+1]
            
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        # create intial and final move
                        initial =  Square(row, col)
                        final  = Square(possible_move_row, possible_move_col)
                        # create new move
                        move = Move(initial, final)
                        piece.add_move(move)
            
        def knight_moves():
            # 8 possibel moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # created squares on the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece
                        # create new move
                        move = Move(initial, final)
                        piece.add_move(move)
                        
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row+ row_incr
                possible_move_col = col + col_incr
                
                while True :
                    if Square.in_range(possible_move_row, possible_move_col):
                        # create  squres of possible new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a possible new mobe
                        move = Move(initial, final)
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # append new movc
                            piece.add_move(move)
                        
                        # has enmey piece 
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            # append move 
                            piece.add_move(move)
                            break
                        # has team piece
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                        
                        
                    else: break
                        
                        # increamenting incr
                    possible_move_row = possible_move_row +row_incr
                    possible_move_col = possible_move_col + col_incr
                    
        
        def king_moves():
            adjs = [
                (row-1, col+0), # up
                (row-1,col+1), # up-right
                (row+0, col+1), # right
                (row+1, col+1), # down-right
                (row+1, col+0), # down
                (row+1, col-1), # down-left
                (row+0, col-1), # left
                (row-1,col-1), # up-left
                    ]
            # normal movw
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # created squares on the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece
                        # create new move
                        move = Move(initial, final)
                        # append new valid move
                        piece.add_move(move)
            
            # castling moves
            
            # Queen castling
            # King Castling 
            
                        
        
        if isinstance(piece, Pawn): 
            pawn_moves()
        elif isinstance(piece, Knight): 
            knight_moves()
        elif isinstance(piece, Bishop):
            straightline_moves(
                [
                    (-1,1) , # up-right
                    (-1,-1), # up-left
                    (1,1), # down-right
                    (1,-1), # down-left
                ]
            )
        elif isinstance(piece, Rook):
            straightline_moves(
                [
                    (-1, 0),# up
                    (0, 1) , # right
                    (1,0), # down
                    (0,-1), # left
                ]
            )
        elif isinstance(piece, Queen):
            straightline_moves(
                [
                    (-1, 0),# up
                    (0, 1) , # right
                    (1,0), # down
                    (0,-1), # left
                    (-1,1) , # up-right
                    (-1,-1) ,# up-left
                    (1,1), # down-right
                    (1,-1), # down-left
                ]
                
                
            )
        elif isinstance(piece, King):
            king_moves()
    
    
    
    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
    
    def _add_piece(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        for col in range(COLS):
            # Here, you need to use square brackets to access the specific element in self.squares
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knight
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))  # Changed 5 to 4
