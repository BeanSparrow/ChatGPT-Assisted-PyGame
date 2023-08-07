import pygame

class EXPBar():
    def __init__(self, screen):
        self.screen = screen
        self.current_experience = 0
        self.max_experience = 100

        self.bar_width = self.screen.get_width() + 4
        self.bar_height = self.screen.get_height() // 60
        self.bar_x = -2
        self.bar_y = self.screen.get_height() - (self.bar_height - 2)

        self.experience_ratio = self.max_experience / self.bar_width

    def experience_bar_draw(self, experience):
        self.current_experience = experience
        experience_bar_rect = pygame.Rect(self.bar_x, self.bar_y, self.current_experience / self.experience_ratio, self.bar_height)
        pygame.draw.rect(self.screen, (0, 255, 0), experience_bar_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.bar_x, self.bar_y, self.bar_width, self.bar_height), 2)


