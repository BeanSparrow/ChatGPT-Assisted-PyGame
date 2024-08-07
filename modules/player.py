import pygame
from .player_modules.weapon import Weapon
from .player_modules.weapon import Pistol
from .player_modules.weapon import MachineGun
from .player_modules.weapon import Shotgun
from .player_modules.scrap_bar import ScrapBar
from .player_modules.health_bar import HealthBar
from .player_modules.crosshair import Crosshair
from .player_modules.potion import Potion

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, screen, modifiers):
        super().__init__()
        #Modifiers
        self.modifiers = modifiers

        # Player Stats
        self.size = 80
        self.scrap_amount = 0
        self.max_health = 100 + self.modifiers.player_max_health
        self.current_health = 100
        self.speed = 5 * self.modifiers.player_speed
        
        # Screen Settings
        self.screen = screen

        # Player Weapon Choice
        self.weapon = Pistol()

        # Player Death Flag
        self.is_dead = False

        # Scrap Bar
        self.scrap_bar = ScrapBar(self.screen)

        # Health Bar
        self.health_bar = HealthBar(self.screen, self.scrap_bar.bar_height)
        self.health_target = 100
 
        # Potion
        self.potion_group = pygame.sprite.Group()
        self.potion = Potion(self.screen, self.scrap_bar.bar_height)
        self.potion_group.add(self.potion)

        # Crosshair
        self.crosshair = Crosshair(self.screen)

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
        self.current_health = self.health_bar.health_bar_draw(self.current_health, self.max_health, self.health_target)
        self.scrap_bar.scrap_bar_draw(self.scrap_amount)
        self.potion_group.draw(self.screen)
        self.potion_group.update()
        self.crosshair.crosshair_draw(self.rect.centerx, self.rect.centery)
  
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
    
    def gain_scrap(self):
        self.scrap_amount += 1 * self.modifiers.scrap_increase

    def take_damage(self, amount):
        if self.health_target> 0:
            self.health_target-= amount
        if self.health_target<= 0:
            self.health_target= 0
            self.is_dead = True
    
    def use_potion(self):
        potion_use = self.potion.trigger()
        if potion_use:
            if self.health_target< self.max_health:
                self.health_target+= self.potion.heal_ammount
            if self.health_target> self.max_health:
                self.health_target= self.max_health

    def reset(self):
        self.health = self.max_health
        self.is_dead = False
        self.weapon = Pistol()