import pygame


class Button():
    def __init__(self, screen, x, y, width, height, defaultColor="white", selectedColor="black"):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = x, y

        self.selectedColor = selectedColor
        self.defaultColor = defaultColor
        self.currentColor = self.defaultColor
        self.wasClicked = False

    def draw(self):
        pygame.draw.rect(self.screen, self.currentColor, self.rect)

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.currentColor = self.selectedColor
        else:
            self.currentColor = self.defaultColor

    def clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return pygame.mouse.get_pressed()[0]
