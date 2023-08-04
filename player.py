import pygame
import math
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width, screen_height):
        super().__init__()
        
        # Player Stats
        self.size = 60
        self.max_health = 10
        self.health = 2
        self.speed = 5
        self.is_dead = False
        
        # Player Sprite
        self.picture_path = "Assets\Img\Player\player_test.png"
        self.image = pygame.image.load(self.picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        
        # Player Facing Direction
        self.direction = (0, 0)  # (dx, dy)
        self.began_moving = False  # Flag to track if the player is moving
        
    def move(self, dx, dy):
        # Calculate the new positions for each point of the triangle
        self.rect.center = (self.rect.centerx + dx, self.rect.centery + dy)

        #Store Player Direction
        self.direction = (dx, dy)

        # Player has started moving, so set the flag to True
        self.began_moving = True
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_dead = True
