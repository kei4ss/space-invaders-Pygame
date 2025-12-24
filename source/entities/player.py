import pygame
from entities.bullet import Bullet, BulletManager


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(50, 500, 25, 25)
        self.playerColor = (255, 128, 0)
        self.speed = 25
        self.life = 3

        self.currentTime = 0
        self.lastTimeMove = 0
        self.lastTimeShoot = 0
        self.timeToMove = 200 # milliseconds
        self.timeToShoot = 500

        self.maxBullets = 5

    def draw(self):
        pygame.draw.rect(self.screen, self.playerColor, self.rect)
        self.current_time = pygame.time.get_ticks()

    def update(self):
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_d] or keysPressed[pygame.K_RIGHT]:
            if self.rect.right < pygame.display.get_window_size()[0]:
                self.__move(plusX=self.speed)
        if keysPressed[pygame.K_a] or keysPressed[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.__move(plusX=-self.speed)
        if keysPressed[pygame.K_SPACE] or keysPressed[pygame.K_UP]:
            if self.current_time - self.lastTimeShoot >= self.timeToShoot and BulletManager.countBullets(self) < self.maxBullets:
                BulletManager.addBullet(Bullet(self.screen, self.rect.center[0], self.rect.center[1], createBy=self))
                self.lastTimeShoot = self.current_time

        if BulletManager.checkCollision(self):
            self.rect = pygame.Rect(50, 500, 25, 25)

    def __move(self, plusX=0):
        if self.current_time - self.lastTimeMove > self.timeToMove:
            x = self.rect.x + plusX
            y = self.rect.y
            width = self.rect.width
            height = self.rect.height
            self.rect.update(x, y, width, height)
            self.lastTimeMove = self.current_time