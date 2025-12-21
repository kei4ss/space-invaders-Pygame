import pygame

class Bullet():
    def __init__(self, screen, x, y, toUp = True):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.rect.center = (x, y)
        self.screen = screen
        self.canDelete = False
        self.speed = 25
        self.toUp = toUp

        self.timeToMove = 200
        self.timeLastTimeMove = 0

    def draw(self):
        pygame.draw.rect(self.screen, "white", self.rect)

    def update(self):
        if self.toUp:
            if pygame.time.get_ticks() - self.timeLastTimeMove > self.timeToMove:
                if self.rect.y > -10:
                    self.rect.update(self.rect.x, self.rect.y - self.speed, self.rect.width, self.rect.height)
                else:
                    self.canDelete = True
                self.timeLastTimeMove = pygame.time.get_ticks()