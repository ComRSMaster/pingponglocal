import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from screenmanager import ScreenManager
from ui import UI, Button, TextView


class MainMenu:
    def __init__(self):
        from screens.game import Game

        with open("save.bin", "rb") as save_file:
            killed = int.from_bytes(save_file.read(), signed=False)
        self.ui = UI([
            TextView(f"Рекорд: {killed}",
                     Vector2(WIDTH / 2, HEIGHT / 2 - 60)),
            Button("Играть",
                   Vector2(WIDTH / 2, HEIGHT / 2 + 60), (300, 80),
                   lambda: ScreenManager.change_screen(Game()))
        ])

    def render(self, screen: pygame.Surface):
        pass

    def process_keys(self, keys):
        pass
