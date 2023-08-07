import pygame

class HealthBar:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.width = self.screen.get_width() // 3
        self.height = self.screen.get_height() // 20
        self.x = self.screen.get_width() // 2 - self.width // 2
        self.y = self.screen.get_height() - ((self.height // 2) + 100)
        self.max_health = player.max_health  # Assuming player has a max_health attribute

        # Calculate the font size based on the height of the health bar
        self.font_size = min(self.width // 2, self.height)
        self.font = pygame.font.Font(None, self.font_size)

    def draw(self):
        health_percentage = self.player.health / self.max_health
        filled_width = int(health_percentage * self.width)

        # Draw the health bar background
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

        # Draw the filled part of the health bar
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, filled_width, self.height))

        # Draw the text
        health_text = f"{self.player.health} / {self.max_health}"
        text_surface = self.font.render(health_text, True, (0, 0, 0))  # Black color
        text_x = self.x + self.width // 2 - text_surface.get_width() // 2
        text_y = self.y - text_surface.get_height() + self.height - 5
        self.screen.blit(text_surface, (text_x, text_y))