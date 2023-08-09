import pygame

class ScrapBar():
    def __init__(self, screen):
        self.screen = screen
        self.current_scrap = 0
        self.max_scrap = 100

        self.bar_width = self.screen.get_width() + 4
        self.bar_height = self.screen.get_height() // 60
        self.bar_x = -2
        self.bar_y = self.screen.get_height() - (self.bar_height - 2)

        self.ratio = self.max_scrap / self.bar_width

    def scrap_bar_draw(self, scrap):
        self.current_scrap = scrap
        scrap_bar_rect = pygame.Rect(self.bar_x, self.bar_y, self.current_scrap / self.ratio, self.bar_height)
        pygame.draw.rect(self.screen, (0, 255, 0), scrap_bar_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.bar_x, self.bar_y, self.bar_width, self.bar_height), 2)


