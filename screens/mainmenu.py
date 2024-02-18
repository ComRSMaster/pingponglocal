import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from screenmanager import ScreenManager
from ui import UI, Button


class MainMenu:
    def __init__(self):
        from screens.game import Game
        self.ui = UI([Button("Играть", Vector2(WIDTH / 2, HEIGHT / 2), lambda: ScreenManager.change_screen(Game()))])

    def render(self, screen: pygame.Surface):
        pass

    def process_keys(self, keys):
        pass
