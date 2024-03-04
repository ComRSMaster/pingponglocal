import math
import random

import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT, FPS
from objects.ball import Ball
from objects.block import Block
from objects.obstacle import Obstacle
from screenmanager import ScreenManager
from screens.gameover import GameOver
from ui import UI, TextView


class Game:
    ball_count = 10
    killed = 0

    def __init__(self):
        self.block = Block()
        self.balls = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

        self.count_text = TextView(str(self.ball_count), Vector2(50, 40))
        self.killed_text = TextView(str(self.killed), Vector2(WIDTH - 50, 40))
        ball_start_speed = 200 / FPS
        for _ in range(self.ball_count):
            ang = random.uniform(-math.pi / 4 * 3, -math.pi / 4)
            Ball(position=Vector2(WIDTH / 2 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2,
                                  HEIGHT / 2 + 150 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2),
                 velocity=Vector2(ball_start_speed * math.cos(ang), ball_start_speed * math.sin(ang)),
                 group=self.balls, on_die=self.on_ball_die)

        for x in range(-1, 2):
            for y in range(-1, 2):
                Obstacle(position=Vector2(WIDTH / 2 + Obstacle.width * x * 1.2, HEIGHT / 2 + Obstacle.height * y * 1.2),
                         group=self.obstacles)

        self.ui = UI([
            self.count_text,
            self.killed_text
        ])

    def on_ball_die(self):
        self.ball_count -= 1
        self.count_text.set_text(str(self.ball_count))

    def render(self, screen: pygame.Surface):
        self.balls.update(self.block)
        self.process_obstacles()

        self.block.render(screen)

        for obstacle in self.obstacles:
            obstacle.render(screen)

        for ball in self.balls:
            ball.render_path(screen)
        for ball in self.balls:
            ball.render(screen)
        # print(self.ball_count)
        if self.ball_count == 0:
            ScreenManager.change_screen(GameOver(self.killed))

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

    def process_obstacles(self):
        collisions = pygame.sprite.groupcollide(self.balls, self.obstacles, 0, 1, pygame.sprite.collide_rect)
        for collision in collisions:
            # print(collision)
            self.killed += 1
            self.killed_text.set_text(str(self.killed))
