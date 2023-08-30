import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
 
class Check:
    def drop_down(self):
        pygame.init()

        screen_width, screen_height = 800, 800
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pawn Promotion")

        promotion_options = ["Queen", "Knight", "Bishop", "Rook"]

        font = pygame.font.Font(None, 24)

        white = (255, 255, 255)
        black = (0, 0, 0)
        gray = (200, 200, 200)

        running = True
        selected_option = None
        show_options = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 10 <= x <= 210 and 10 <= y <= 30:
                        show_options = not show_options
                    elif show_options and 10 <= x <= 210:
                        for i, option in enumerate(promotion_options):
                            if 30 + i * 30 <= y <= 30 + (i + 1) * 30:
                                selected_option = option
                                running = False

            screen.fill(black)

            text_surface = font.render("Promotion", True, white)
            screen.blit(text_surface, (20, 10))
            pygame.draw.rect(screen, white, (10, 10, 200, 20), 2)

            if selected_option is not None:
                selected_text = font.render(f"Selected: {selected_option}", True, white)
                screen.blit(selected_text, (20, 60))
            else:
                pygame.draw.rect(screen, white, (10, 10, 200, 20))
                text_surface = font.render("Options", True, black)
                screen.blit(text_surface, (20, 10))
                if show_options:
                    for i, option in enumerate(promotion_options):
                        pygame.draw.rect(screen, gray, (10, 30 + i * 30, 200, 30))
                        text_surface = font.render(option, True, black)
                        screen.blit(text_surface, (20, 30 + i * 30))

            pygame.display.flip()
            pygame.time.Clock().tick(30)

        return selected_option


if __name__ == "__main__":
    ch = Check()
    ch.drop_down()
