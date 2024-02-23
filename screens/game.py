import math
import random

import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from objects.ball import Ball
from objects.block import Block
from objects.obstacle import Obstacle
from screenmanager import ScreenManager
from ui import UI, TextView


class Game:
    ball_count = 10
    def __init__(self):
        self.block = Block()
        self.balls = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

        self.count_text = TextView(str(self.ball_count), Vector2(50, 40))
        for _ in range(self.ball_count):
            ang = random.random() * 2 * math.pi
            Ball(position=Vector2(WIDTH / 2 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2,
                                  HEIGHT / 2 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2),
                 velocity=Vector2(2 * math.cos(ang), 2 * math.sin(ang)),
                 group=self.balls, on_die=lambda: self.count_text.set_text(str(int(self.count_text.text) - 1)))

        for x in range(-1, 2):
            for y in range(-1, 2):
                Obstacle(position=Vector2(WIDTH / 2 + Obstacle.width * x * 1.2, HEIGHT / 2 + Obstacle.height * y * 1.2),
                         group=self.obstacles)

        self.ui = UI([
            self.count_text
        ])

    def render(self, screen: pygame.Surface):
        self.balls.update(self.block)

        self.block.render(screen)

        for obstacle in self.obstacles:
            obstacle.render(screen)

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
