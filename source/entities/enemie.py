import random

import pygame
from config.direction import Direction, Border
from config.gameStage import Stage
from entities.bullet import BulletManager, Bullet
from entities.player import Player


class Enemie:
    def __init__(self, display, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.display = display
        self.speed = 30
        self.enemieColor = (0, 204, 255)
        self.border = None

    def draw(self):
        pygame.draw.rect(self.display, self.enemieColor, self.rect)

    def update(self, direction):
        x, y = self.rect.x, self.rect.y
        width, height = self.rect.width, self.rect.height
        if direction == Direction.LEFT:
            self.rect.update(x - self.speed, y, width, height)
            self.border = Border.LEFT if self.rect.left - self.speed <= 0 else None
        elif direction == Direction.RIGHT:
            self.rect.update(x + self.speed, y, width, height)
            self.border = Border.RIGHT if self.rect.right + self.speed >= pygame.display.get_window_size()[0] else None
        elif direction == Direction.DOWN:
            self.rect.update(x, y + self.speed, width, height)

    def getRect(self):
        return self.rect

    def getBorderContact(self):
        return self.border


class ShooterEnemie(Enemie):
    def __init__(self, display, x, y):
        super().__init__(display, x, y)
        self.enemieColor = (255, 0, 153)
        self.lastTimeShoot = pygame.time.get_ticks()
        self.timeToShoot = random.randint(3000, 10000)

    def draw(self):
        if pygame.time.get_ticks() - self.lastTimeShoot >= self.timeToShoot:
            BulletManager.addBullet(Bullet(self.display, self.rect.centerx, self.rect.centery, createBy=self, targets=[Player],  toUp=False))
            self.lastTimeShoot = pygame.time.get_ticks()
        super().draw()



class EnemieManage:
    def __init__(self, display):
        self.board = Stage.STAGE_1.value
        self.currentPhase = 0
        self.arrivedFinalStage = False
        self.initalPos = (0, 50)
        self.display = display

        self.lastTimeMoved = 0
        self.timeToMove = 1000
        self.direction = Direction.RIGHT
        self.lastDirectionBeforeDown = None
        self.needDown = False

        self.enemies = []

    def draw(self):
        for index in range(len(self.enemies)):
            self.enemies[index].draw()

    def update(self):
        if pygame.time.get_ticks() - self.lastTimeMoved > self.timeToMove:
            if self.needDown:
                self.lastDirectionBeforeDown = self.direction
                self.direction = Direction.DOWN
                self.timeToMove = self.timeToMove - 50
                print("time: ", self.timeToMove)

            for index in range(len(self.enemies)):
                self.enemies[index].update(self.direction)
                if self.enemies[index].getBorderContact() is not None and not self.needDown:
                    self.needDown = True

            if self.direction == Direction.DOWN:
                if self.lastDirectionBeforeDown == Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif self.lastDirectionBeforeDown == Direction.LEFT:
                    self.direction = Direction.RIGHT
                self.needDown = False
                self.lastDirectionBeforeDown = None

            if len(self.enemies) == 0:
                if self.currentPhase < Stage.TOTAL_STAGES.value:
                    self.currentPhase += 1
                    match self.currentPhase:
                        case 2:
                            self.board = Stage.STAGE_2.value
                        case 3:
                            self.board = Stage.STAGE_3.value
                        case 4:
                            self.board = Stage.STAGE_4.value
                            self.arrivedFinalStage = True
                    self.createEnemies()
            self.lastTimeMoved = pygame.time.get_ticks()



        enemies = [enemie.getRect() for enemie in self.enemies]
        index = BulletManager.checkCollisionList(enemies)
        if index is not None:
            self.enemies.pop(index)

    def createEnemies(self):
        for line in range(len(self.board)):
            for collum in range(len(self.board[line])):
                spaceBeetweenEnemeies = 45
                x = (self.initalPos[0] + spaceBeetweenEnemeies * collum)
                y = (self.initalPos[1] + spaceBeetweenEnemeies * line)
                if self.board[line][collum] == 'x':
                    self.enemies.append(Enemie(self.display, x, y))
                if self.board[line][collum] == 'y':
                    self.enemies.append(ShooterEnemie(self.display, x, y))

        self.direction = Direction.RIGHT
        self.lastDirectionBeforeDown = None
        self.needDown = False
        self.timeToMove = 1000

    def isGameOver(self):
        return self.arrivedFinalStage