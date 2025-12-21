import pygame
from config.direction import Direction, Border

class Enemie():
    def __init__(self, display, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.display = display
        self.direction = Direction.LEFT
        self.speed = 25

        self.enemieColor = "white"

        self.border = None

    def draw(self):
        pygame.draw.rect(self.display, self.enemieColor, self.rect)

    def update(self):
        x, y = self.rect.x, self.rect.y
        width, height = self.rect.width, self.rect.height
        if self.direction == Direction.LEFT:
            self.rect.update(x + self.speed, y, width, height)
        elif self.direction == Direction.RIGHT:
            self.rect.update(x - self.speed, y, width, height)
        elif self.direction == Direction.DOWN:
            self.rect.update(x, y + self.speed, width, height)

    def changeDirection(self, direction):
        self.direction = direction

class ShooterEnemie(Enemie):
    def __init__(self, display, x, y):
        super().__init__(display, x, y)
        self.enemieColor = "red"


class EnemieManage():
    def __init__(self, display):
        self.board = [
            ['x', 'y', 'x', 'y', 'x', 'y', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'y', 'x', 'x', 'x'],
            ['x', 'y', 'x', 'x', 'x', 'y', 'x']
        ]
        self.initalPos = (50, 50)
        self.display = display
        self.enemies = []

        self.lastTimeMoved = 0
        self.timeToMove = 700

        self.reset()

    def draw(self):
        for index in range(len(self.enemies)):
            self.enemies[index].draw()
    def update(self):
        if pygame.time.get_ticks() - self.lastTimeMoved > self.timeToMove:
            for index in range(len(self.enemies)):
                self.enemies[index].update()
            self.lastTimeMoved = pygame.time.get_ticks()

    def reset(self):
        self.enemies = []

        for line in range(len(self.board)):
            for collum in range(len(self.board[line])):
                x = (self.initalPos[1] + 40 * collum)
                y = (self.initalPos[0] + 40 * line)
                if self.board[line][collum] == 'x':
                    self.enemies.append(Enemie(self.display, x, y))
                if self.board[line][collum] == 'y':
                    self.enemies.append(ShooterEnemie(self.display, x, y))



