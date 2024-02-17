import random

import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from objects.ball import Ball
from objects.block import Block


class Game:
    def __init__(self):
        self.block = Block()
        self.balls = [
            Ball(position=Vector2(WIDTH / 2 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2,
                                  HEIGHT / 2 + (random.random() - 0.5) * Block.MOVE_RADIUS / 1.2),
                 velocity=Vector2((random.random() - 0.5) * 3, (random.random() - 0.5) * 3)) for _ in range(1)]
        self.frame_counter = 0

    def render(self, screen: pygame.Surface):
        self.frame_counter += 1
        for ball in self.balls:
            ball.process_physics(self.block)

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
