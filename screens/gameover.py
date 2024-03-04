import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from screenmanager import ScreenManager
from ui import UI, Button, TextView


class GameOver:
    def __init__(self, killed: int):
        from screens.game import Game

        self.ui = UI([
            TextView("Игра окончена",
                     Vector2(WIDTH / 2, HEIGHT / 2 - 150)),
            TextView(f"Блоков убито: {killed}",
                     Vector2(WIDTH / 2, HEIGHT / 2 - 60)),
            Button("Играть снова",
                   Vector2(WIDTH / 2, HEIGHT / 2 + 60), (300, 80),
                   lambda: ScreenManager.change_screen(Game()))
        ])
        with open("save.bin", "wb") as save_file:
            save_file.write(killed.to_bytes(32, signed=False))

    def render(self, screen: pygame.Surface):
        pass

    def process_keys(self, keys):
        pass
