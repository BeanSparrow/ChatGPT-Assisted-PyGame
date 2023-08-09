import pygame

class HealthBar():
    def __init__(self, screen, exp_bar_height):
        # Health Bar Stats
        self.screen = screen
        self.exp_bar_height = exp_bar_height
        self.width = self.screen.get_width() // 3
        self.height = self.screen.get_height() // 20
        self.x = 0
        self.y = self.screen.get_height() - (self.height + self.exp_bar_height - 2)
        self.health_change_speed = .25

    def health_bar_draw(self, current_health, max_health, health_target):
        transition_color = (0,0,0)
        health_ratio = max_health / self.width
        health_bar_rect = pygame.Rect(self.x, self.y, health_target / health_ratio, self.height)
        if current_health < health_target:
            current_health += self.health_change_speed
            transition_color = (0,255,0)
            transition_width = abs(current_health - health_target) / health_ratio
            transition_bar_rect = pygame.Rect(health_bar_rect.right - transition_width, self.y, transition_width, self.height)
        elif current_health > health_target:
            current_health -= self.health_change_speed
            transition_color = (255,255,0)
            transition_bar_rect = pygame.Rect(health_bar_rect.right, self.y, (current_health - health_target) / health_ratio, self.height)
        else:
            transition_bar_rect = pygame.Rect(health_bar_rect.right, 1000, 0, 25)

        pygame.draw.rect(self.screen, (255, 0, 0), health_bar_rect)
        pygame.draw.rect(self.screen, transition_color, transition_bar_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 4)

        self.health_text(current_health, max_health)
        
        return current_health

    def health_text(self, current_health, max_health):
        # Draw health text
        font_size = int(self.height * 0.6)  # 60% of the health bar's height
        font = pygame.font.Font(None, font_size)
        health_text = f"{int(current_health)} / {max_health}"
        text_color = (255, 255, 255)  # White
        border_color = (0, 0, 0)  # Black
        border_size = 2

        # Calculate the position of the text
        text_x = self.x + (self.width - font.size(health_text)[0]) // 2
        text_y = self.y + (self.height - font.size(health_text)[1]) // 2

        # Render the text with a border
        for dx, dy in [(x, y) for x in range(-border_size, border_size + 1) for y in range(-border_size, border_size + 1)]:
            text_surface = font.render(health_text, True, border_color)
            self.screen.blit(text_surface, (text_x + dx, text_y + dy))

        # Render the text in the original color
        text_surface = font.render(health_text, True, text_color)
        self.screen.blit(text_surface, (text_x, text_y))