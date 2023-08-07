#region #### LIBRARIES ####  
# Import Libraries
import pygame
import sys
import math
import random
from player import Player
from enemy import Enemy
from exp_coin import EXPCoin
from menus import create_main_menu
from menus import create_weapon_selection_menu
from menus import show_game_over_screen
from menus import show_pause_menu
from hud import draw_score
from hud import draw_timer
from settings import Settings
#endregion

#region #### PYGAME INITIALIZE ####
# Initialize Pygame
pygame.init()

def initialize_game(game):
    # Reset player and enemy states
    game.player.reset()
    game.enemy_sprites.empty()
    game.bullet_sprites.empty()
    game.exp_coins_sprites.empty()
    game.settings.score = 0
    game.settings.game_over_condition = False
    game.settings.total_game_time = 0
    game.settings.paused = False
    # Other reset logic can be added here as needed

#endregion

#region #### EVENTS ####
playerDeath = pygame.USEREVENT + 1
enemyHit = pygame.USEREVENT + 2
playerHit = pygame.USEREVENT + 3
expPickup = pygame.USEREVENT +  4
#endregion

#region #### GLOBAL SETTINGS ####
# Get the current screen resolution
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
#endregion

#region #### GAME CLASS ####
class Game:
    #region #### GAME INITIALIZATION ####
    def __init__(self):
        # Set up the display in fullscreen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Untitled Hoard Shooter")

        # Creating Settings
        self.settings = Settings(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Create the player
        self.player_group = pygame.sprite.Group()
        self.player = Player(self.settings.screen_width, self.settings.screen_height, self.screen)
        self.player_group.add(self.player)

        # Store Enemies
        self.enemy_sprites = pygame.sprite.Group()
        
        # Store Bullets
        self.bullet_sprites = pygame.sprite.Group()

        # Store Exp Coins
        self.exp_coins_sprites = pygame.sprite.Group()

        # Timer for auto-firing bullets
        self.fire_timer = 0
        self.fire_interval = 1000  # 1000 milliseconds = 1 second

        # Collision Event
        self.enemy_hit = False
        self.player_hit = False
        self.player_gained_exp = False
        self.enemy_collisions = {}  # Dictionary to store enemy collisions
        self.player_collisions = {}  # Dictionary to store player collisions
        self.exp_pickup_collision = {} # Dictionary to store XP Collisions
    #endregion
    
    #region #### GAME METHODS ####
    #region #### EVENT HANDLING ####
    def handle_enemy_spawning(self, dt):
        # Check if it's time to spawn a new enemy
        self.settings.enemy_timer += dt
        if self.settings.enemy_timer >= self.settings.enemy_interval and len(self.enemy_sprites.sprites()) < self.settings.max_enemies:
            enemy = Enemy(self.settings.screen_width, self.settings.screen_height)
            enemy.set_initial_position()
            self.settings.enemy_timer = 0
            self.enemy_sprites.add(enemy)
    
    def handle_events(self):
        # Custom Events
        if self.player.is_dead:
            pygame.event.post(pygame.event.Event(playerDeath))
        if self.enemy_hit:
            pygame.event.post(pygame.event.Event(enemyHit))
        if self.player_hit:
            pygame.event.post(pygame.event.Event(playerHit))
        if self.player_gained_exp:
            pygame.event.post(pygame.event.Event(expPickup))
        
        # Get Current Time
        current_time = pygame.time.get_ticks()
        
        # Event handling
        for event in pygame.event.get():
            # Quit Game on 'ESC' key press
            if event.type == pygame.QUIT:
                self.quit_game()
            # End Game on Player Death    
            if event.type == playerDeath:
                self.settings.game_over_condition = True
            # Handle Enemy Hit
            if event.type == enemyHit:
                for bullet, enemies in self.enemy_collisions.items():
                    for enemy in enemies:
                        death = enemy.take_damage(self.player.weapon.damage)
                        if death:
                            self.settings.score += enemy.score_value
                            exp_coin = EXPCoin(enemy.rect.centerx, enemy.rect.centery)
                            self.exp_coins_sprites.add(exp_coin)
                self.enemy_hit = False
                self.enemy_collisions = {}
            # Handle Player Hit
            if event.type == playerHit:
                for player, enemies in self.player_collisions.items():
                    for enemy in enemies:
                        player.take_damage(enemy.damage)
                        enemy.kill()
                self.player_hit = False
                self.player_collisions = {}
            # Handle EXP Pickup
            if event.type == expPickup:
                for player, exp_coins in self.exp_pickup_collision.items():
                    for exp in exp_coins:
                        exp.kill()
                        player.experience += 1
                self.player_gained_exp = False
                self.exp_pickup_collision = {}

        # Keyboard input handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and current_time - self.settings.last_pause_time >= self.settings.pause_cooldown:
            self.settings.paused = not self.settings.paused  # Toggle the pause state
            self.settings.last_pause_time = current_time  # Update the last key time
        if keys[pygame.K_w]:
            self.player.move(0, -self.player.speed)
        if keys[pygame.K_s]:
            self.player.move(0, self.player.speed)
        if keys[pygame.K_a]:
            self.player.move(-self.player.speed, 0)
        if keys[pygame.K_d]:
            self.player.move(self.player.speed, 0)
        # Debugging Events
        if keys[pygame.K_1]:
            self.player.get_heal(10)
        if keys[pygame.K_2]:
            self.player.take_damage(10)
        if keys[pygame.K_3]:
            print(self.player.experience)

    def quit_game(self):
        pygame.quit()
        sys.exit()
    #endregion

    #region #### COLLISION DETECTION ####
    def collision_check(self):
        bullet_collisions = pygame.sprite.groupcollide(self.bullet_sprites, self.enemy_sprites, True, False)
        if bullet_collisions:
            self.enemy_hit = True
            self.enemy_collisions = bullet_collisions

        player_collision = pygame.sprite.groupcollide(self.player_group, self.enemy_sprites, False, True)
        if player_collision:
            self.player_hit = True
            self.player_collisions = player_collision

        exp_pickup_collision = pygame.sprite.groupcollide(self.player_group, self.exp_coins_sprites, False, False)
        if exp_pickup_collision:
            self.player_gained_exp = True
            self.exp_pickup_collision = exp_pickup_collision
    #endregion
    
    #region #### UPDATES ####
    def update(self):
        # Move and draw the enemy sprites
        self.enemy_sprites.update(self.player.rect.centerx, self.player.rect.centery, self.screen)
        self.enemy_sprites.draw(self.screen)

        # Move and draw the bullets
        self.bullet_sprites.update()
        self.bullet_sprites.draw(self.screen)

        # Draw Exp Coins
        self.exp_coins_sprites.update(self.player.rect.centerx, self.player.rect.centery)
        self.exp_coins_sprites.draw(self.screen)

        for bullet in self.bullet_sprites:
            if bullet.distance_traveled >= bullet.max_distance:
                bullet.kill()
        
        # Draw and update the player
        self.player_group.update()
        self.player_group.draw(self.screen)

        draw_score(game)
        draw_timer(game)

    def fireBulletUpdate(self):
        # Fire bullets only when the player is moving
        if self.player.began_moving:
            bullets = self.player.weapon.fire(self.player.rect.centerx, self.player.rect.centery, self.player.direction)
            for bullet in bullets:
                self.bullet_sprites.add(bullet)

    #endregion

    #region #### DRAWING ####
    def draw(self):
        # Fill the screen with white
        self.screen.fill(BLACK)

        # Collision Check
        self.collision_check()
        # Update Game State
        self.update()

        # Update the display
        pygame.display.flip()
    #endregion

    #region #### MAIN GAME LOOP ####
    def game_loop(self):
        # Main game loop
        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(60)  # Limit frame rate to 60 FPS
            self.handle_events()
            
            if not self.settings.paused:
                self.settings.total_game_time += dt
                self.handle_enemy_spawning(dt)
                self.draw()
                
                # Auto-fire bullets
                self.settings.fire_timer += clock.get_time()
                if self.settings.fire_timer >= self.player.weapon.fire_interval:
                    self.fireBulletUpdate()
                    self.settings.fire_timer = 0
                
                if self.settings.game_over_condition:
                    restart_choice = show_game_over_screen(self.screen, self.settings.screen_width, self.settings.screen_height)
                    if restart_choice == "restart":
                        initialize_game(self)
                        return "restart"
                    else:
                        break
            else:
                pause_restart_choice = show_pause_menu(game)
                if pause_restart_choice == "restart":
                    initialize_game(self)
                    return "restart"
    #endregion
    #endregion
#endregion

#region #### MAIN FUNCTION ####

if __name__ == "__main__":
    game = Game()
    # Run the main menu loop until the player selects "Play Game" or "Quit"
    while True:
        play = create_main_menu(game)

        # If the player selects "Play Game," start the game loop
        if play == "play":
            while True:
                weapon = create_weapon_selection_menu(game)
                if weapon != "back":
                    game.player.set_weapon(weapon)
                    result = game.game_loop()
                    if result != "restart":
                        break
                else:
                    break
#endregion