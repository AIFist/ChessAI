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
        
        
        while True:
            game.show_bg(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
    
    
    
main = Main()
main.mainloop()