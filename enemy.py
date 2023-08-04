import pygame
import math
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.picture_path = "Assets\Img\Enemy\Robot\Robot_move_right.png"
        self.size = 60
        self.image = pygame.image.load(self.picture_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect(center=(width // 2, height // 2))
        self.speed = 1
        self.screen_width = width
        self.screen_height = height
        self.health = 1

    def set_initial_position(self):
        # Choose a random side of the screen (0=top, 1=right, 2=bottom, 3=left)
        side = random.randint(0, 3)
    
        if side == 0:  # Top side
            self.rect.centerx = random.randint(0, self.screen_width)
            self.rect.centery = 0
        elif side == 1:  # Right side
            self.rect.centerx = self.screen_width
            self.rect.centery = random.randint(0, self.screen_height)
        elif side == 2:  # Bottom side
            self.rect.centerx = random.randint(0, self.screen_width)
            self.rect.centery = self.screen_height
        else:  # Left side
            self.rect.centerx = 0
            self.rect.centery = random.randint(0, self.screen_height)
    
    def take_damage(self, damage):
        self.health -= damage

    def move(self, player_x, player_y):
        dx = player_x - self.rect.centerx
        dy = player_y - self.rect.centery
        distance_to_player = max(1, math.hypot(dx, dy))
        dx /= distance_to_player
        dy /= distance_to_player

        self.rect.centerx += dx * self.speed
        self.rect.centery += dy * self.speed

    def update(self, playerx, playery):
        self.move(playerx, playery)

    