import pygame
import sys
from const import *
from game import Game
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        
    def mainloop(self):
        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger
        
        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_piece(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    
                    
                    # if click square has piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        # show methos
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_piece(screen)
                        
                        
                
                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show method
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_piece(screen)
                        dragger.update_blit(screen)
                #Click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                # quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
    
    
    
main = Main()
main.mainloop()