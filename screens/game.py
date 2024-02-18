import math
import random

import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from objects.ball import Ball
from objects.block import Block
from screenmanager import ScreenManager
from ui import UI


class Game:
    def __init__(self):
        self.block = Block()
        self.balls = pygame.sprite.Group()
        for _ in range(500):
            ang = random.random() * 2 * math.pi
            Ball(position=Vector2(WIDTH / 2 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2,
                                  HEIGHT / 2 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2),
                 velocity=Vector2(2 * math.cos(ang), 2 * math.sin(ang)),
                 group=self.balls)
        self.ui = UI([])

    def render(self, screen: pygame.Surface):
        self.balls.update(self.block)

        self.block.render(screen)

        for ball in self.balls:
            ball.render_path(screen)
        for ball in self.balls:
            ball.render(screen)

    def process_keys(self, keys):
        if keys[pygame.K_LEFT]:
            self.block.delta_move(-1)
        if keys[pygame.K_RIGHT]:
            self.block.delta_move(1)
        if keys[pygame.K_r]:
            ScreenManager.change_screen(Game())
        if keys[pygame.K_ESCAPE]:
            from screens.mainmenu import MainMenu
            ScreenManager.change_screen(MainMenu())
