import pygame
import math

class Crosshair:
    def __init__(self, screen):
        self.screen = screen
        self.size = 50
        self.radius = self.screen.get_width() // 20
        self.image = pygame.image.load("Assets\Img\Crosshair\crosshair_style1.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size)).convert_alpha()
        self.last_crosshair_dx = 1
        self.last_crosshair_dy = 1
    
    def get_crosshair_dx_dy(self, playerx, playery):
        # Check for Joystick
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)  # Assuming you want to use the first joystick
            joystick.init()

            # Get the horizontal and vertical values from the second analog stick
            # Note: The axis indices (2 and 3) might need to be adjusted depending on the controller
            dx = joystick.get_axis(2)
            dy = joystick.get_axis(3)

            # If there's minimal joystick input (to avoid drift), keep the crosshair at its current position
            if abs(dx) < 0.4 and abs(dy) < 0.4:
                return self.last_crosshair_dx, self.last_crosshair_dy
        else:
            # Fallback to Mouse Position if no joystick is detected
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - playerx
            dy = mouse_y - playery


        # Normalize the direction vector
        length = math.sqrt(dx * dx + dy * dy)
        if length != 0:
            dx /= length
            dy /= length

        self.last_crosshair_dx = dx
        self.last_crosshair_dy = dy
        return dx, dy
    
    def get_crosshair_x_y(self, playerx, playery):
        # Calculate the crosshair's position maintaining a fixed distance (radius) from the player
        dx,dy = self.get_crosshair_dx_dy(playerx, playery)       
        crosshair_x = playerx + dx * self.radius
        crosshair_y = playery + dy * self.radius
        return crosshair_x, crosshair_y

    def crosshair_draw(self, playerx, playery):
        crosshair_x, crosshair_y = self.get_crosshair_x_y(playerx, playery)

        self.screen.blit(self.image, (crosshair_x - self.image.get_width() / 2, crosshair_y - self.image.get_height() / 2))
    