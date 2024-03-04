import math
from collections import deque
from typing import Callable

import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT, FPS
from objects.block import Block


class Ball(pygame.sprite.Sprite):
    GRAVITY = Vector2(0, 1 / FPS)
    PATH_SIZE = 60
    SCREEN_BOX = pygame.Rect(0, 0, WIDTH, HEIGHT)

    def __init__(self,
                 position: Vector2,
                 velocity: Vector2,
                 group: pygame.sprite.Group,
                 on_die: Callable):
        super().__init__()
        self.radius = 4
        self.pos = position
        self.vel = velocity
        self.arrow = deque(maxlen=self.PATH_SIZE)
        self.arrow.append(self.pos.__copy__())
        self.add(group)

        self.image = None
        self.rect = pygame.Rect(position.x - self.radius, position.y - self.radius, self.radius, self.radius)
        self.on_die = on_die

        self.in_zone = True
        self.is_bounced = False

    def render_path(self, screen: pygame.Surface):
        pygame.draw.lines(screen, '#444444', False, self.arrow, 1)

    def render(self, screen: pygame.Surface):
        # if frame_counter % 100 == 0:

        # for (ind, (left, right)) in enumerate(pairwise(self.arrow)):
        pygame.draw.circle(screen, 'white', self.pos, self.radius)

    def update(self, block: Block):
        self.pos += self.vel
        self.rect.update(self.pos.x - self.radius, self.pos.y - self.radius, self.radius, self.radius)
        self.vel += self.GRAVITY
        self.arrow.append(self.pos.__copy__())
        dist_to_center = self.pos.distance_to((WIDTH / 2, HEIGHT / 2))
        if self.in_zone:
            if dist_to_center >= Block.MOVE_RADIUS - self.radius:
                y = math.atan2(self.vel.x, self.vel.y)
                to_center = self.pos - Block.CENTER
                a = math.atan2(to_center.y, to_center.x)
                b = -block.angle % (2 * math.pi)
                if min(abs(b - a), abs(b - 2 * math.pi - a)) > Block.BLOCK_WIDTH:
                    if dist_to_center > Block.MOVE_RADIUS:
                        # die
                        self.in_zone = False
                        self.on_die()
                elif not self.is_bounced:
                    self.vel.rotate_ip_rad(2 * y + 2 * a)
                    self.is_bounced = True
            else:
                self.is_bounced = False
        elif not self.SCREEN_BOX.collidepoint(self.pos) or dist_to_center <= Block.MOVE_RADIUS:
            self.kill()

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
