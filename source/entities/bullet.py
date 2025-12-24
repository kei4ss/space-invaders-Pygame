import pygame

class Bullet():
    def __init__(self, screen, x, y, createBy ,targets=None, toUp = True):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.rect.center = (x, y)
        self.screen = screen
        self.canDelete = False
        self.speed = 25
        self.toUp = toUp
        self.createBy = createBy
        self.targets = targets

        self.timeToMove = 100
        self.timeLastTimeMove = 0

    def draw(self):
        pygame.draw.rect(self.screen, "white", self.rect)

    def update(self):
        if pygame.time.get_ticks() - self.timeLastTimeMove > self.timeToMove:
            if self.toUp:
                if self.rect.y > -10:
                    self.rect.update(self.rect.x, self.rect.y - self.speed, self.rect.width, self.rect.height)
                else:
                    self.canDelete = True
            else:
                if self.rect.y < pygame.display.get_window_size()[1]:
                    self.rect.update(self.rect.x, self.rect.y + self.speed, self.rect.width, self.rect.height)
                else:
                    self.canDelete = True
            self.timeLastTimeMove = pygame.time.get_ticks()

    def getRect(self):
        return self.rect

class BulletManager():
    bulletList = []

    @staticmethod
    def addBullet(bullet):
        BulletManager.bulletList.append(bullet)
        print("Bala de ", bullet.createBy.__class__.__name__)

    @staticmethod
    def update(screen):
        for index in range(len(BulletManager.bulletList)):
            BulletManager.bulletList[index].update()
            BulletManager.bulletList[index].draw()
            if BulletManager.bulletList[index].canDelete:
                BulletManager.bulletList.pop(index)
                break

    @staticmethod
    def checkCollisionList(targets):
        for bullet in BulletManager.bulletList:
            index = bullet.getRect().collidelist(targets)
            if index != -1:
                if bullet.targets is None:
                    if bullet.createBy != targets[index]:
                        BulletManager.bulletList.remove(bullet)
                        return index
                else:
                    for targetType in bullet.targets:
                        if isinstance(targets[index], targetType):
                            print("ele colidiu com um", type(targetType[index]))
                            return index


        return None

    @staticmethod
    def checkCollision(target):
        for bullet in BulletManager.bulletList:
            if bullet.rect.colliderect(target):
                if bullet.targets is not None:
                    for t in bullet.targets:
                        if isinstance(target, t):
                            BulletManager.bulletList.remove(bullet)
                            return True
                else:
                    if bullet.createBy != target:
                        BulletManager.bulletList.remove(bullet)
                        return True

        return False


    @staticmethod
    def countBullets(target):
        count = 0
        for bullet in BulletManager.bulletList:
            if bullet.createBy == target:
                count += 1
        return count

    @staticmethod
    def resetBulletList():
        BulletManager.bulletList = []


