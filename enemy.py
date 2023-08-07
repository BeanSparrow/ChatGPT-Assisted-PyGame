import pygame
import math
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        # Enemy Stats
        self.size = 60
        self.radius = self.size // 2
        self.speed = 1
        self.current_health = 20
        self.max_health = 20
        self.score_value = 1
        self.damage = 10
        
        # Animation Values
        self.tick_count = 0
        self.switch_interval = 30 
        
        #  Screen Stats
        self.screen_width = width
        self.screen_height = height
        
        # Load multiple sprites for different directions
        self.image_left1 = pygame.transform.scale(pygame.image.load("Assets\Img\Enemy\Robot\\robot_move_left.png").convert_alpha(), (self.size, self.size))
        self.image_left2 = pygame.transform.scale(pygame.image.load("Assets\Img\Enemy\Robot\\robot_move_left_extend.png").convert_alpha(), (self.size, self.size))
        self.image_up1 = pygame.transform.scale(pygame.image.load("Assets\Img\Enemy\Robot\\robot_left_updown.png").convert_alpha(), (self.size, self.size))
        self.image_up2 = pygame.transform.scale(pygame.image.load("Assets\Img\Enemy\Robot\\robot_left_updown_extend.png").convert_alpha(), (self.size, self.size))
        
         # Create sprites for right and down directions by flipping the left and up sprites
        self.image_right1 = pygame.transform.flip(self.image_left1, True, False)
        self.image_right2 = pygame.transform.flip(self.image_left2, True, False)
        self.image_down1 = pygame.transform.flip(self.image_up1, True, False)
        self.image_down2 = pygame.transform.flip(self.image_up2, True, False)
        
         # Start with default images
        self.image_right = self.image_right1
        self.image_left = self.image_left1
        self.image_up = self.image_up1
        self.image_down = self.image_down1
        self.image = self.image_right
        
        self.rect = self.image.get_rect(center=(width // 2, height // 2))


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
        self.current_health -= damage
        if self.current_health <= 0:
            self.kill()
            return True
        else:
            return False

    def move(self, player_x, player_y):
        old_centerx = self.rect.centerx
        old_centery = self.rect.centery

        dx = player_x - self.rect.centerx
        dy = player_y - self.rect.centery
        distance_to_player = max(1, math.hypot(dx, dy))
        dx /= distance_to_player
        dy /= distance_to_player

        self.rect.centerx += dx * self.speed
        self.rect.centery += dy * self.speed

        # Increment tick count
        self.tick_count += 1
        if self.tick_count >= self.switch_interval:
            # Switch images
            if self.image_right == self.image_right1:
                self.image_right = self.image_right2
                self.image_left = self.image_left2
                self.image_up = self.image_up2
                self.image_down = self.image_down2
            else:
                self.image_right = self.image_right1
                self.image_left = self.image_left1
                self.image_up = self.image_up1
                self.image_down = self.image_down1

            # Reset tick count
            self.tick_count = 0

        # Determine direction based on old and new positions
        delta_x = self.rect.centerx - old_centerx
        delta_y = self.rect.centery - old_centery

        if abs(delta_x) > abs(delta_y):  # Moving more horizontally than vertically
            if delta_x > 0:  # Moving right
                self.image = self.image_right
            else:  # Moving left
                self.image = self.image_left
        else:  # Moving more vertically than horizontally
            if delta_y > 0:  # Moving down
                self.image = self.image_down
            else:  # Moving up
                self.image = self.image_up

    def draw_health_bar(self, screen):
        padding = 10
        offset = self.radius + padding
        if self.current_health != self.max_health:
            bar_width = 50
            bar_height = 5
            health_width = (self.current_health / self.max_health) * bar_width
            health_color = (0, 255, 0)  # Green
            background_color = (255, 0, 0)  # Red
            pygame.draw.rect(screen, background_color, (self.rect.centerx - self.radius, self.rect.centery - offset, bar_width, bar_height))
            pygame.draw.rect(screen, health_color, (self.rect.centerx - self.radius, self.rect.centery - offset, health_width, bar_height))

    def update(self, playerx, playery, screen):
        self.move(playerx, playery)
        self.draw_health_bar(screen)

    