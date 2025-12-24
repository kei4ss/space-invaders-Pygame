import pygame
from os import path
from config.gameModes import GameModes
from entities.bullet import BulletManager
from entities.button import Button
from entities.player import Player
from entities.enemie import EnemieManage

pygame.init()

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((700, 600))
        pygame.display.set_caption("Keias invaders")
        self.logoImage = pygame.image.load(path.join("..", "midia", "img","logo.png"))

        self.game_mode = GameModes.MENU
        self.tick = pygame.time.Clock()

        self.buttonStart = Button(self.display, 350, 450, 150, 50, selectedColor="green")
        self.buttonGoMenu = Button(self.display, 620, 25, 80, 25, defaultColor="cyan", selectedColor="blue")
        self.player = Player(self.display)
        self.enemies = EnemieManage(self.display)

    def run(self):
        running = True
        while running:
            self.tick.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            match self.game_mode:
                case GameModes.MENU:
                    self.menuScreen()
                case GameModes.GAME:
                    self.gameScreen()

            pygame.display.update()

    def menuScreen(self):
        self.display.fill('black')
        self.display.blit(self.logoImage, (100, 50))
        self.buttonStart.draw()
        self.buttonStart.update()

        if self.buttonStart.clicked():
            self.resetEntities()
            self.game_mode = GameModes.GAME

    def gameScreen(self):
        self.display.fill((0, 0, 0))

        self.buttonGoMenu.update()
        self.player.update()
        self.enemies.update()
        BulletManager.update(self.display)

        self.enemies.draw()
        self.buttonGoMenu.draw()
        self.player.draw()

        if self.buttonGoMenu.clicked():
            self.game_mode = GameModes.MENU
            self.resetEntities()

    def resetEntities(self):
        self.player = Player(self.display)
        self.enemies = EnemieManage(self.display)
        BulletManager.resetBulletList()

if __name__ == "__main__":
    game = Game()
    game.run()
