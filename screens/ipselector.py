import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from screenmanager import ScreenManager
from ui import UI, Button, TextInput, TextView
import socket


class IPSelector():
    def __init__(self):
        from screens.game import Game

        self.ui = UI([
            TextView(f"Ваш IP адрес:\n{socket.gethostbyname(socket.gethostname())}", Vector2(WIDTH / 2, HEIGHT / 2 - 160)),
            Button("Открыть сервер", Vector2(WIDTH / 2, HEIGHT / 2 - 60), (400, 80),
                   lambda: ScreenManager.change_screen(Game())),
            TextInput("Введите адрес",
                      Vector2(WIDTH / 2, HEIGHT / 2 + 60), (400, 80)),
            Button("Подключиться",
                   Vector2(WIDTH / 2, HEIGHT / 2 + 190), (400, 80),
                   lambda: ScreenManager.change_screen(Game())),
        ])

    def render(self, screen: pygame.Surface):
        pass

    def process_keys(self, keys):
        pass
