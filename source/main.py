import pygame
import os
from config.gameModes import GameModes
from entities.button import Button
from entities.player import Player
from entities.enemie import EnemieManage

pygame.init()

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Space invaders - Miquéias game")
        self.logoImage = pygame.image.load(os.path.join("..", "midia", "img","logo.png"))

        self.game_mode = GameModes.MENU
        self.tick = pygame.time.Clock()

        self.buttonStart = Button(self.display, 250, 350, 150, 50, selectedColor="green")
        self.buttonGoMenu = Button(self.display, 420, 25, 100, 25, defaultColor="cyan", selectedColor="blue")
        self.player = Player(self.display)
        self.enemies = EnemieManage(self.display)

    def run(self):
        running = True
        while running:
            self.tick.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.game_mode == GameModes.MENU:
                self.menuScreen()

            elif self.game_mode == GameModes.GAME:
                self.gameScreen()

            pygame.display.update()

    def menuScreen(self):
        self.display.fill((0,0,0))
        self.display.blit(self.logoImage, (90, 50))
        self.buttonStart.draw()
        self.buttonStart.update()

        if self.buttonStart.clicked():
            self.game_mode = GameModes.GAME

    def gameScreen(self):
        self.display.fill((0, 0, 0))

        self.buttonGoMenu.update()
        self.player.update()
        self.enemies.update()

        self.enemies.draw()
        self.buttonGoMenu.draw()
        self.player.draw()

        if self.buttonGoMenu.clicked():
            self.game_mode = GameModes.MENU
            self.player.reset()
            self.enemies.reset()


if __name__ == "__main__":
    game = Game()
    game.run()
