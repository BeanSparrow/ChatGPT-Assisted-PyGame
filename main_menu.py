import pygame
import sys

def create_main_menu(self):
        # Main menu loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            self.screen.fill((128, 128, 128))

            # Draw the main menu buttons
            play_button_rect = pygame.Rect(self.screen_width / 2, (self.screen_height / 2) - 100, 200, 50)
            quit_button_rect = pygame.Rect(self.screen_width / 2, (self.screen_height / 2) + 100, 200, 50)

            pygame.draw.rect(self.screen, (0, 255, 0), play_button_rect)
            pygame.draw.rect(self.screen, (255, 0, 0), quit_button_rect)

            font = pygame.font.Font(None, 36)
            play_text = font.render("Play Game", True, (0, 0, 0))
            quit_text = font.render("Quit", True, (0, 0, 0))

            self.screen.blit(play_text, (play_button_rect.centerx - play_text.get_width() // 2, play_button_rect.centery - play_text.get_height() // 2))
            self.screen.blit(quit_text, (quit_button_rect.centerx - quit_text.get_width() // 2, quit_button_rect.centery - quit_text.get_height() // 2))

            pygame.display.flip()

            # Check for button clicks
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if play_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
                return "play"
            elif quit_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
                self.quit_game()