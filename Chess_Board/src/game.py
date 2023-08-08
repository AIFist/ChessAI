import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self) -> None:
        self.next_player = 'white'
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()
    # show methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) %2 ==0:
                    color = (234,235, 200) # light green
                else:
                  color = (119,154,88) # dark green
                
                rect = (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
                
                pygame.draw.rect(surface, color, rect)
                
    def show_piece(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    
                    # all pieces exepct dragger piece 
                    
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE +  SQSIZE //2, row * SQSIZE +SQSIZE //2 
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)
    
    def show_moves(self, surface):
        
        if self.dragger.dragging:
            
            piece = self.dragger.piece

            # loop all valid move
            for move in piece.moves:
                # color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # rect
                rect = (move.final.col*SQSIZE, move.final.row *SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
                
    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial 
            final = self.board.last_move.final 
            
            for pos in [initial, final]:
                # color
                color = (244,247,116) if (pos.row + pos.col) % 2 == 0 else (172,195,51)
                # rect
                rect = (pos.col *SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
    
    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col *SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect,width=3)
            
                
    # other functions
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'
        
    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]