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
        self.gameOverButton = Button(self.display, 350, 300, 150, 50, defaultColor= "red", selectedColor="blue")
        self.player = Player(self.display)
        self.enemies = EnemieManage(self.display)

        self.font_1 = pygame.font.Font(None, 25)

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
                case GameModes.GAME_OVER:
                    self.gameOverScreen()

            pygame.display.update()

    def menuScreen(self):
        self.display.fill('black')
        self.display.blit(self.logoImage, (100, 50))
        self.buttonStart.draw()
        self.buttonStart.update()

        if self.buttonStart.clicked():
            self.resetEntities()
            self.game_mode = GameModes.GAME

    def gameOverScreen(self):
        self.display.fill('black')
        self.gameOverButton.update()
        self.gameOverButton.draw()

        if self.gameOverButton.clicked():
            self.game_mode = GameModes.MENU


    def gameScreen(self):
        self.display.fill((0, 0, 0))

        if not self.player.isAlive():
            self.game_mode = GameModes.GAME_OVER
            return

        self.buttonGoMenu.update()
        self.player.update()
        self.enemies.update()
        BulletManager.update(self.display)

        self.enemies.draw()
        self.buttonGoMenu.draw()
        self.player.draw()

        playerLifeText = self.font_1.render(f"Lifes: {self.player.life}", True, (255, 255, 255))
        self.display.blit(playerLifeText, (10, 10))

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
