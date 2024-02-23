import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from screenmanager import ScreenManager
from ui import UI, Button


class MainMenu:
    def __init__(self):
        from screens.game import Game
        from screens.ipselector import IPSelector

        self.ui = UI([
            Button("Играть",
                   Vector2(WIDTH / 2, HEIGHT / 2 - 60), (300, 80),
                   lambda: ScreenManager.change_screen(Game())),
            Button("Игра по сети",
                   Vector2(WIDTH / 2, HEIGHT / 2 + 60), (300, 80),
                   lambda: ScreenManager.change_screen(IPSelector())),
        ])

    def render(self, screen: pygame.Surface):
        pass

    def process_keys(self, keys):
        pass
