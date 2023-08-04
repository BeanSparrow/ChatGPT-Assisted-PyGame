import pygame

class GameOverScreen:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.button_width = 120
        self.button_height = 50
        self.button_radius = 10
        self.button_depth = 8
        self.restart_button = pygame.Rect(width / 2 - self.button_width / 2, height / 2 + 100, self.button_width, self.button_height)
        self.quit_button = pygame.Rect(width / 2 - self.button_width / 2, height / 2 + 300, self.button_width, self.button_height)
        self.game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        self.restart_text = self.font.render("Restart", True, (0, 0, 0))
        self.quit_text = self.font.render("Quit", True, (0, 0, 0))

    def show_game_over(self):
        self.screen.fill((255, 0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.restart_button.collidepoint(pygame.mouse.get_pos()):
                        return "restart"
                    elif self.quit_button.collidepoint(pygame.mouse.get_pos()):
                        pygame.quit()
                        quit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.game_over_text, (self.width // 2 - 50, self.height // 2 - 100))
            
            # Draw restart button
            pygame.draw.rect(self.screen, (150, 150, 150), self.restart_button)
            pygame.draw.rect(self.screen, (100, 100, 100), self.restart_button.inflate(-self.button_depth, -self.button_depth))
            pygame.draw.rect(self.screen, (200, 200, 200), self.restart_button.move(self.button_depth, self.button_depth))
            pygame.draw.rect(self.screen, (0, 255, 0), self.restart_button, border_radius=self.button_radius)
            self.screen.blit(self.restart_text, (self.width / 2 - 50, self.height / 2 + 100))
            
            # Draw quit button
            pygame.draw.rect(self.screen, (150, 150, 150), self.quit_button)
            pygame.draw.rect(self.screen, (100, 100, 100), self.quit_button.inflate(-self.button_depth, -self.button_depth))
            pygame.draw.rect(self.screen, (200, 200, 200), self.quit_button.move(self.button_depth, self.button_depth))
            pygame.draw.rect(self.screen, (255, 0, 0), self.quit_button, border_radius=self.button_radius)
            self.screen.blit(self.quit_text, (self.width / 2 - 50, self.height / 2 + 300))
            
            pygame.display.flip()