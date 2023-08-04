import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 2
        self.direction = direction
        self.size = 5
        self.color = (255, 215, 0)
        self.image = pygame.surface.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.distance_traveled = 0
        self.max_distance = 200

    def move(self):
        self.rect.centerx += self.direction[0] * self.speed
        self.rect.centery += self.direction[1] * self.speed
        self.distance_traveled += self.speed

    def update(self):
        self.move()