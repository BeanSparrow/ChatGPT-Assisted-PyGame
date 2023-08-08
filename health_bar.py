import pygame

class HealthBar():
    def __init__(self, screen, exp_bar_height):
        # Health Bar Stats
        self.screen = screen
        self.exp_bar_height = exp_bar_height
        self.health_bar_width = self.screen.get_width() // 3
        self.health_bar_height = self.screen.get_height() // 20
        self.health_bar_x = 0
        self.health_bar_y = self.screen.get_height() - (self.health_bar_height + self.exp_bar_height - 2)
        self.health_change_speed = .25

    def health_bar_draw(self, current_health, max_health, health_target):
        transition_color = (0,0,0)
        health_ratio = max_health / self.health_bar_width
        health_bar_rect = pygame.Rect(self.health_bar_x, self.health_bar_y, health_target / health_ratio, self.health_bar_height)
        if current_health < health_target:
            current_health += self.health_change_speed
            transition_color = (0,255,0)
            transition_width = abs(current_health - health_target) / health_ratio
            transition_bar_rect = pygame.Rect(health_bar_rect.right - transition_width, self.health_bar_y, transition_width, self.health_bar_height)
        elif current_health > health_target:
            current_health -= self.health_change_speed
            transition_color = (255,255,0)
            transition_bar_rect = pygame.Rect(health_bar_rect.right, self.health_bar_y, (current_health - health_target) / health_ratio, self.health_bar_height)
        else:
            transition_bar_rect = pygame.Rect(health_bar_rect.right, 1000, 0, 25)

        pygame.draw.rect(self.screen, (255, 0, 0), health_bar_rect)
        pygame.draw.rect(self.screen, transition_color, transition_bar_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.health_bar_x, self.health_bar_y, self.health_bar_width, self.health_bar_height), 4)

        self.health_text(current_health, max_health)
        
        return current_health

    def health_text(self, current_health, max_health):
        # Draw health text
        font_size = int(self.health_bar_height * 0.6)  # 60% of the health bar's height
        font = pygame.font.Font(None, font_size)
        health_text = f"{int(current_health)} / {max_health}"
        text_color = (255, 255, 255)  # White
        border_color = (0, 0, 0)  # Black
        border_size = 2

        # Calculate the position of the text
        text_x = self.health_bar_x + (self.health_bar_width - font.size(health_text)[0]) // 2
        text_y = self.health_bar_y + (self.health_bar_height - font.size(health_text)[1]) // 2

        # Render the text with a border
        for dx, dy in [(x, y) for x in range(-border_size, border_size + 1) for y in range(-border_size, border_size + 1)]:
            text_surface = font.render(health_text, True, border_color)
            self.screen.blit(text_surface, (text_x + dx, text_y + dy))

        # Render the text in the original color
        text_surface = font.render(health_text, True, text_color)
        self.screen.blit(text_surface, (text_x, text_y))


