import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, distance, size, speed):
        super().__init__()
        
        # Bullet Stats
        self.speed = speed
        self.direction = direction
        self.size = size
        self.max_distance = distance
        self.distance_traveled = 0
        
        # Visual
        self.color = (255, 215, 0)
        self.image = pygame.surface.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        
        # Position
        self.rect.center = (x, y)

    def move(self):
        self.rect.centerx += self.direction[0] * self.speed
        self.rect.centery += self.direction[1] * self.speed
        self.distance_traveled += self.speed

    def update(self):
        self.move()