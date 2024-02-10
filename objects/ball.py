import math
from math import atan2

import pygame

from constants import WIDTH, HEIGHT
from objects.block import Block


class Ball:
    SPEED = 0.8

    def __init__(self):
        self.radius = 30
        self.pos = pygame.math.Vector2(WIDTH / 2, HEIGHT / 2)
        self.vel = pygame.math.Vector2(self.SPEED, -self.SPEED)

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, 'white', self.pos, self.radius)
        # pygame.draw.rect(screen, 'red',
        #                  pygame.rect.Rect(self.pos.x - self.radius,
        #                                   self.pos.y - self.radius,
        #                                   self.radius * 2,
        #                                   self.radius * 2))

    def process_physics(self, block: Block):
        self.pos += self.vel
        if self.pos.distance_to((WIDTH / 2, HEIGHT / 2)) >= block.MOVE_RADIUS - self.radius:
            self.vel *= -1

    # def process_physics(self, block: pygame.Rect):
    #     self.pos += self.vel
    #     # if not in_x and not in_y:
    #     #     r2 = self.radius ** 2
    #     #     if self.pos.distance_squared_to(block.bottomright) <= r2:
    #     #         a = math.atan2(self.pos.x - block.right, self.pos.y - block.bottom)
    #     #         b = math.atan2(-self.vel.y, self.vel.x)
    #     #         print(a, b)
    #     #         self.vel.update(self.SPEED * math.cos(2 * a - b), self.SPEED * math.sin(2 * a - b))
    #     #         return
    #
    #     # with block
    #     x1 = block.right - self.pos.x + self.radius
    #     x2 = self.pos.x + self.radius - block.right
    #     x3 = block.left - self.pos.x + self.radius
    #     x4 = self.pos.x + self.radius - block.left
    #     y1 = block.top - self.pos.y + self.radius
    #     y2 = self.pos.y + self.radius - block.top
    #     y3 = block.bottom - self.pos.y + self.radius
    #     y4 = self.pos.y + self.radius - block.bottom
    #     if block.top - self.radius < self.pos.y < block.bottom + self.radius:
    #         if x1 >= 0 and x2 >= 0 and min(x1, x2) < min(r3, r4):
    #             self.vel.x *= -1
    #             self.pos.x = block.right + self.radius
    #         elif x3 >= 0 and x4 >= 0 and min(r3, r4) < min(r1, r2):
    #             self.vel.x *= -1
    #             self.pos.x = block.left - self.radius
    #     if block.left - self.radius < self.pos.x < block.right + self.radius:
    #         if y1 >= 0 and y2 >= 0 and self.vel.y > 0:
    #             self.vel.y *= -1
    #             self.pos.y = block.top - self.radius
    #         elif y3 >= 0 and y4 >= 0 and self.vel.y < 0:
    #             self.vel.y *= -1
    #             self.pos.y = block.bottom + self.radius
    #
    #     # with wall
    #     if self.pos.x < self.radius:
    #         self.vel.x *= -1
    #         self.pos.x = self.radius
    #     elif self.pos.x > WIDTH - self.radius:
    #         self.vel.x *= -1
    #         self.pos.x = WIDTH - self.radius
    #     if self.pos.y < self.radius:
    #         self.pos.y = self.radius
    #         self.vel.y *= -1
    #     elif self.pos.y > HEIGHT - self.radius:
    #         self.pos.y = HEIGHT - self.radius
    #         self.vel.y *= -1
