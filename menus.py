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

def create_weapon_selection_menu(self):
    # Weapon selection menu loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

        self.screen.fill((128, 128, 128))

        # Draw the weapon selection buttons
        pistol_button_rect = pygame.Rect(self.screen_width / 3, (self.screen_height / 3) - 100, 200, 50)
        machinegun_button_rect = pygame.Rect(self.screen_width / 3, self.screen_height / 3, 200, 50)
        shotgun_button_rect = pygame.Rect(self.screen_width / 3, (self.screen_height / 3) + 100, 200, 50)
        back_button_rect = pygame.Rect(self.screen_width / 3, (self.screen_height / 3) + 200, 200, 50)

        pygame.draw.rect(self.screen, (0, 255, 0), pistol_button_rect)
        pygame.draw.rect(self.screen, (0, 255, 0), machinegun_button_rect)
        pygame.draw.rect(self.screen, (0, 255, 0), shotgun_button_rect)
        pygame.draw.rect(self.screen, (255, 0, 0), back_button_rect)

        font = pygame.font.Font(None, 36)
        pistol_text = font.render("Pistol", True, (0, 0, 0))
        machinegun_text = font.render("Machine Gun", True, (0, 0, 0))
        shotgun_text = font.render("Shotgun", True, (0, 0, 0))
        back_text = font.render("Back", True, (0, 0, 0))

        self.screen.blit(pistol_text, (pistol_button_rect.centerx - pistol_text.get_width() // 2, pistol_button_rect.centery - pistol_text.get_height() // 2))
        self.screen.blit(machinegun_text, (machinegun_button_rect.centerx - machinegun_text.get_width() // 2, machinegun_button_rect.centery - machinegun_text.get_height() // 2))
        self.screen.blit(shotgun_text, (shotgun_button_rect.centerx - shotgun_text.get_width() // 2, shotgun_button_rect.centery - shotgun_text.get_height() // 2))
        self.screen.blit(back_text, (back_button_rect.centerx - back_text.get_width() // 2, back_button_rect.centery - back_text.get_height() // 2))

        pygame.display.flip()

        # Check for button clicks
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if pistol_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            return "Pistol"
        elif machinegun_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            return "MachineGun"
        elif shotgun_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            return "Shotgun"
        elif back_button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            return "back"
        
def show_game_over_screen(screen, width, height):
    font = pygame.font.Font(None, 36)
    button_width = 120
    button_height = 50
    button_radius = 10
    button_depth = 8
    restart_button = pygame.Rect(width / 2 - button_width / 2, height / 2 + 100, button_width, button_height)
    quit_button = pygame.Rect(width / 2 - button_width / 2, height / 2 + 300, button_width, button_height)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    restart_text = font.render("Restart", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))

    screen.fill((255, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(pygame.mouse.get_pos()):
                    return "restart"
                elif quit_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        screen.fill((0, 0, 0))
        screen.blit(game_over_text, (width // 2 - 50, height // 2 - 100))

        # Draw restart button
        pygame.draw.rect(screen, (150, 150, 150), restart_button)
        pygame.draw.rect(screen, (100, 100, 100), restart_button.inflate(-button_depth, -button_depth))
        pygame.draw.rect(screen, (200, 200, 200), restart_button.move(button_depth, button_depth))
        pygame.draw.rect(screen, (0, 255, 0), restart_button, border_radius=button_radius)
        screen.blit(restart_text, (width / 2 - 50, height / 2 + 100))

        # Draw quit button
        pygame.draw.rect(screen, (150, 150, 150), quit_button)
        pygame.draw.rect(screen, (100, 100, 100), quit_button.inflate(-button_depth, -button_depth))
        pygame.draw.rect(screen, (200, 200, 200), quit_button.move(button_depth, button_depth))
        pygame.draw.rect(screen, (255, 0, 0), quit_button, border_radius=button_radius)
        screen.blit(quit_text, (width / 2 - 50, height / 2 + 300))

        pygame.display.flip()