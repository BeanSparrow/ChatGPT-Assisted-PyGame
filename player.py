import pygame
from weapon import Weapon
from weapon import Pistol
from weapon import MachineGun
from weapon import Shotgun
from exp_bar import EXPBar
from health_bar import HealthBar

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, screen):
        super().__init__()
        # Player Stats
        self.size = 60
        self.experience = 0
        self.max_health = 100
        self.current_health = 100
        self.speed = 5
        self.is_dead = False
        self.screen = screen
        self.weapon = Pistol()

        # Experience Bar
        self.exp_bar = EXPBar(self.screen)

        # Health Bar
        self.health_bar = HealthBar(self.screen, self.exp_bar.bar_height)
        self.health_target = 100

        # Player Sprite
        self.picture_path = "Assets\Img\Player\player_test.png"
        self.image = pygame.image.load(self.picture_path).convert_alpha()
        self.images_left = [pygame.image.load('Assets\Img\Player\player_left1.png'), pygame.image.load('Assets\Img\Player\player_left2.png')]
        self.images_right = [pygame.transform.flip(image, True, False) for image in self.images_left]
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)

        # Animation Counter
        self.current_image = 0
        self.move_counter = 0
        
        # Player Facing Direction
        self.direction = (0, 0)  # (dx, dy)
        self.began_moving = False  # Flag to track if the player is moving

    def update(self):
        self.health_bar.health_bar_draw(self.current_health, self.max_health, self.health_target)
        self.exp_bar.experience_bar_draw(self.experience)
  
    def move(self, dx, dy):
        # Calculate the new positions for each point of the triangle
        self.rect.center = (self.rect.centerx + dx, self.rect.centery + dy)

        #Store Player Direction
        self.direction = (dx, dy)

        # Player has started moving, so set the flag to True
        self.began_moving = True

        if self.move_counter >= 10:
            self.move_counter = 0
            self.current_image = (self.current_image + 1) % len(self.images_left)
        
        if dx < 0:
            self.image = pygame.transform.scale(self.images_left[self.current_image], (self.size, self.size))
        elif dx > 0:
            self.image = pygame.transform.scale(self.images_right[self.current_image], (self.size, self.size))
    
        self.move_counter += 1
    
    def set_weapon(self, weapon):
        if weapon == "Pistol":
            self.weapon = Pistol()
        elif weapon == "MachineGun":
            self.weapon = MachineGun()
        elif weapon == "Shotgun":
            self.weapon = Shotgun()

    def take_damage(self, amount):
        if self.health_target> 0:
            self.health_target-= amount
        if self.health_target<= 0:
            self.health_target= 0
            self.is_dead = True
    
    def get_heal(self, amount):
        if self.health_target< self.max_health:
            self.health_target+= amount
        if self.health_target> self.max_health:
            self.health_target= self.max_health

    def reset(self):
        self.health = self.max_health
        self.is_dead = False
        self.weapon = Pistol()