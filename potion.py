import pygame

class Potion(pygame.sprite.Sprite):
    def __init__(self, screen, exp_bar_height):
        super().__init__()
        # Potion Stats
        self.padding = 5
        self.screen = screen
        self.exp_bar_height = exp_bar_height
        self.height = self.screen.get_height() // 20
        self.width = self.height
        self.centerx = self.screen.get_width() // 3 + (self.width //2) + self.padding
        self.centery = self.screen.get_height() - ((self.height // 2) + self.exp_bar_height - 2)
        self.x = self.screen.get_width() // 3 + self.padding
        self.y = self.screen.get_height() - (self.height + self.exp_bar_height - 2)
        self.image = pygame.transform.scale(pygame.image.load("Assets\Img\Potion\health_potion.png").convert_alpha(), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.centerx, self.centery)
    
    def update(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 4)
        pass

    