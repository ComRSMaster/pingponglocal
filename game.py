import pygame

from constants import WIDTH, HEIGHT
from objects.ball import Ball
from objects.block import Block


class Game:
    def __init__(self):
        self.block = Block()
        self.ball = Ball()

    def render(self, screen: pygame.Surface):
        self.ball.process_physics(self.block)

        self.block.render(screen)
        self.ball.render(screen)

    def process_keys(self, keys):
        if keys[pygame.K_LEFT]:
            self.block.delta_move(-1)
        if keys[pygame.K_RIGHT]:
            self.block.delta_move(1)
