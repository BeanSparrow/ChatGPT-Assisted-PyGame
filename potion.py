import pygame
import math

class Potion(pygame.sprite.Sprite):
    def __init__(self, screen, exp_bar_height):
        super().__init__()
        # Potion Stats
        self.heal_ammount = 10
        self.max_cooldown = 5000 #In Milliseconds
        self.cooldown_remaining = 0  # current cooldown value

        # Potion Image Settings
        self.padding = 5
        self.screen = screen
        self.exp_bar_height = exp_bar_height
        self.height = self.screen.get_height() // 10
        self.width = self.height
        self.centerx = self.screen.get_width() - ((self.width //2) + self.padding)
        self.centery = self.screen.get_height() - ((self.height // 2) + self.exp_bar_height - 2)
        self.x = self.screen.get_width() - self.width - self.padding
        self.y = self.screen.get_height() - (self.height + self.exp_bar_height - 2)
        self.image = pygame.transform.scale(pygame.image.load("Assets\Img\Potion\health_potion.png").convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.centerx, self.centery)
    
    def update(self):
        # Draw the potion itself
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 4)
        
        # Draw the cooldown overlay
        if self.cooldown_remaining > 0:
            cooldown_height = int((self.cooldown_remaining / self.max_cooldown) * self.height)
            cooldown_rect = pygame.Rect(self.x, self.y, self.width, cooldown_height)
            overlay = pygame.Surface((cooldown_rect.width, cooldown_rect.height), pygame.SRCALPHA)
            overlay.fill((100, 100, 100, 128))  # RGBA: semi-transparent gray
            self.screen.blit(overlay, (self.x, self.y))
            self.reduce_cooldown()

         # Calculate the cooldown time in seconds with two decimal places and render as text
            cooldown_seconds = self.cooldown_remaining / 1000
            # cooldown_text = self.font.render(f"{cooldown_seconds:.2f}", True, (255, 0, 0))
            # text_rect = cooldown_text.get_rect(center=self.rect.center)
            # self.screen.blit(cooldown_text, text_rect.topleft)

                # Draw health text
            font_size = int(self.height * 0.4)  # 60% of the health bar's height
            font = pygame.font.Font(None, font_size)
            cooldown_text = f"{cooldown_seconds:.2f}"
            text_color = (255, 255, 255)  # White
            border_color = (0, 0, 0)  # Black
            border_size = 2

            # Calculate the position of the text
            text_x = self.x + (self.width - font.size(cooldown_text)[0]) // 2
            text_y = self.y + (self.height - font.size(cooldown_text)[1]) // 2

            # Render the text with a border
            for dx, dy in [(x, y) for x in range(-border_size, border_size + 1) for y in range(-border_size, border_size + 1)]:
                text_surface = font.render(cooldown_text, True, border_color)
                self.screen.blit(text_surface, (text_x + dx, text_y + dy))

            # Render the text in the original color
            text_surface = font.render(cooldown_text, True, text_color)
            self.screen.blit(text_surface, (text_x, text_y))

    def trigger(self):
        if self.cooldown_remaining == 0:
            self.cooldown_remaining = self.max_cooldown
            return True
        else:
            return False

    def reduce_cooldown(self):
        self.cooldown_remaining -= self.max_cooldown/((self.max_cooldown / 1000) * 60)
        if self.cooldown_remaining < 0:
            self.cooldown_remaining = 0

    