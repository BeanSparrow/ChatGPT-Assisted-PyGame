#region #### LIBRARIES ####  
# Import Libraries
import pygame
import sys
import math
import random
from player import Player
from bullet import Bullet
from enemy import Enemy
from main_menu import create_main_menu
from game_over_screen import GameOverScreen
#endregion

#region #### PYGAME INITIALIZE ####
# Initialize Pygame
pygame.init()

#endregion

#region #### EVENTS ####
playerDeath = pygame.USEREVENT + 1
enemyHit = pygame.USEREVENT + 2
playerHit = pygame.USEREVENT + 3
#endregion

#region #### GLOBAL SETTINGS ####
# Get the current screen resolution
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
#endregion

#region #### GAME CLASS ####
class Game:
    #region #### GAME INITIALIZATION ####
    def __init__(self):
        # Set up the display settings
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

        # Set up the display in fullscreen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Untitled Hored Shooter")

        # Create the player and enemy objects
        self.player_group = pygame.sprite.Group()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.player_group.add(self.player)

        self.enemy_sprites = pygame.sprite.Group()
        self.max_enemies = 5  # The maximum number of enemies to create
        self.enemies_spawned = 0  # The number of enemies that have been spawned
        
        # Store Bullets
        self.bullet_sprites = pygame.sprite.Group()
        
        # Timer for auto-firing bullets
        self.fire_timer = 0
        self.fire_interval = 1000  # 1000 milliseconds = 1 second

        # Game over screen
        self.game_over_screen = GameOverScreen(self.screen, self.screen_width, self.screen_height)

        # Collision Event
        self.enemy_hit = False
        self.player_hit = False
        self.enemy_collisions = {}  # Dictionary to store enemy collisions
        self.player_collisions = {}  # Dictionary to store player collisions
        
        #Score Counter
        self.score = 0

    #endregion
    
    #region #### GAME METHODS ####
    #region #### EVENT HANDLING ####
    def handle_enemy_spawning(self):
        # Check if it's time to spawn a new enemy
        if self.enemies_spawned < self.max_enemies:
            enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemy.set_initial_position()
            self.enemy_sprites.add(enemy)
            self.enemies_spawned += 1
    
    def handle_events(self):
        # Custom Events
        if self.player.is_dead:
            pygame.event.post(pygame.event.Event(playerDeath))
        if self.enemy_hit:
            pygame.event.post(pygame.event.Event(enemyHit))
        if self.player_hit:
            pygame.event.post(pygame.event.Event(playerHit))
        
        # Event handling
        for event in pygame.event.get():
            # Quit Game on 'ESC' key press
            if event.type == pygame.QUIT:
                self.quit_game()
            # End Game on Player Death    
            if event.type == playerDeath:
                self.game_over_screen.show_game_over()
                pygame.time.wait(3000)  # Wait for 3 seconds before quitting
                self.quit_game()
            # Handle Enemy Hit
            if event.type == enemyHit:
                for bullet, enemies in self.enemy_collisions.items():
                    for enemy in enemies:
                        enemy.take_damage(1)
                        if enemy.health <= 0:
                            self.score += 1
                            enemy.kill()
                self.enemy_hit = False
                self.enemy_collisions = {}
            # Handle Player Hit
            if event.type == playerHit:
                for player, enemies in self.player_collisions.items():
                    player.take_damage(1)
                    for enemy in enemies:
                        enemy.kill()
                self.player_hit = False
                self.player_collisions = {}

        # Keyboard input handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.quit_game()
        if keys[pygame.K_w]:
            self.player.move(0, -self.player.speed)
        if keys[pygame.K_s]:
            self.player.move(0, self.player.speed)
        if keys[pygame.K_a]:
            self.player.move(-self.player.speed, 0)
        if keys[pygame.K_d]:
            self.player.move(self.player.speed, 0)

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
    #endregion
    
    #region #### UPDATES ####
    def update(self):
        # Move and draw the enemy sprites
        self.enemy_sprites.update(self.player.rect.centerx, self.player.rect.centery)
        self.enemy_sprites.draw(self.screen)

        # Move and draw the bullets
        self.bullet_sprites.update()
        self.bullet_sprites.draw(self.screen)

        for bullet in self.bullet_sprites:
            if bullet.distance_traveled >= bullet.max_distance:
                bullet.kill()


    def fireBulletUpdate(self):
        # Fire bullets only when the player is moving
        if self.player.began_moving:
            bullet = Bullet(self.player.rect.centerx, self.player.rect.centery, self.player.direction)
            self.bullet_sprites.add(bullet)

    #endregion

    #region #### DRAWING ####
    def draw(self):
        # Fill the screen with white
        self.screen.fill(GRAY)

        # Draw the player
        self.player_group.draw(self.screen)

        # Collision Check
        self.collision_check()
        # Update Game State
        self.update()

        # Draw the score on the top left corner
        font = pygame.font.Font(None, 72)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))  # Display score at (10, 10)

        # Update the display
        pygame.display.flip()
    #endregion

    #region #### MAIN GAME LOOP ####
    def game_loop(self):
        # Main game loop
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.handle_enemy_spawning()
            self.draw()
            
            # Auto-fire bullets
            self.fire_timer += clock.get_time()
            if self.fire_timer >= self.fire_interval:
                self.fireBulletUpdate()
                self.fire_timer = 0

            clock.tick(60)  # Limit frame rate to 60 FPS
    #endregion
    
    #endregion
#endregion

#region #### MAIN FUNCTION ####

if __name__ == "__main__":
    game = Game()

    # Run the main menu loop until the player selects "Play Game" or "Quit"
    while True:
        choice = create_main_menu(game)

        # If the player selects "Play Game," start the game loop
        if choice == "play":
            game.game_loop()
#endregion