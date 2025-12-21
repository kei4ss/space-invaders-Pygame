import pygame

class Enemie():
    def __init__(self, display, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.display = display

    def draw(self):
        pygame.draw.rect(self.display, (0, 255, 0), self.rect)

    def update(self):
        ...

