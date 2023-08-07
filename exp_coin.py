import pygame
import math

class EXPCoin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Enemy Stats
        self.picture_path = "Assets\Img\Experience\XP_coin.png"
        self.size = 30
        self.x = x
        self.y = y
        self.speed = 10

         # Load multiple sprites for different directions
        self.image = pygame.transform.scale(pygame.image.load(self.picture_path).convert_alpha(), (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, player_x, player_y):
        dx = player_x - self.rect.centerx
        dy = player_y - self.rect.centery
        distance_to_player = max(1, math.hypot(dx, dy))
        
        if distance_to_player < 200:
            dx /= distance_to_player
            dy /= distance_to_player

            self.rect.centerx += dx * self.speed
            self.rect.centery += dy * self.speed
    
    def update(self, player_x, player_y):
        self.move(player_x, player_y)

