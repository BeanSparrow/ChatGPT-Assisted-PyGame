import pygame

class EXPCoin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Enemy Stats
        self.picture_path = "Assets\Img\Experience\XP_coin.png"
        self.size = 30
        self.x = x
        self.y = y

         # Load multiple sprites for different directions
        self.image = pygame.transform.scale(pygame.image.load(self.picture_path).convert_alpha(), (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



