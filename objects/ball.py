import math
from collections import deque

import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT
from objects.block import Block


# def drawLineWidth(surface, color, p1, p2, width):
#     # delta vector
#     d = (p2[0] - p1[0], p2[1] - p1[1])
#
#     # distance between the points
#     dis = math.hypot(*d)
#
#     # normalized vector
#     n = (d[0]/dis, d[1]/dis)
#
#     # perpendicular vector
#     p = (-n[1], n[0])
#
#     # scaled perpendicular vector (vector from p1 & p2 to the polygon's points)
#     sp = (p[0]*width/2, p[1]*width/2)
#
#     # points
#     p1_1 = (p1[0] - sp[0], p1[1] - sp[1])
#     p1_2 = (p1[0] + sp[0], p1[1] + sp[1])
#     p2_1 = (p2[0] - sp[0], p2[1] - sp[1])
#     p2_2 = (p2[0] + sp[0], p2[1] + sp[1])
#
#     # draw the polygon
#     pygame.gfxdraw.aapolygon(surface, (p1_1, p1_2, p2_2, p2_1), color)
#     pygame.gfxdraw.filled_polygon(surface, (p1_1, p1_2, p2_2, p2_1), color)

class Ball:
    GRAVITY = Vector2(0, .001)
    PATH_SIZE = 80

    def __init__(self, position: Vector2, velocity: Vector2):
        self.radius = 5
        self.pos = position
        self.vel = velocity
        self.arrow = deque(maxlen=self.PATH_SIZE)
        self.arrow.append(self.pos.__copy__())
        self.in_zone = True

    def render_path(self, screen: pygame.Surface):
        pygame.draw.lines(screen, '#444444', False, self.arrow, 1)

    def render(self, screen: pygame.Surface):
        # if frame_counter % 100 == 0:

        # for (ind, (left, right)) in enumerate(pairwise(self.arrow)):
        pygame.draw.circle(screen, 'white', self.pos, self.radius)

    def process_physics(self, block: Block):
        self.pos += self.vel
        self.vel += self.GRAVITY
        self.arrow.append(self.pos.__copy__())
        if self.in_zone:
            if self.pos.distance_to((WIDTH / 2, HEIGHT / 2)) >= Block.MOVE_RADIUS - self.radius:
                y = math.atan2(self.vel.x, self.vel.y)
                to_center = self.pos - Block.CENTER
                a = math.atan2(to_center.y, to_center.x)
                # if block.angle % (2 * math.pi) < math.pi:
                #     ang =
                if abs(a + math.pi - block.angle % (2 * math.pi)) > Block.BLOCK_WIDTH:
                    self.in_zone = False
                else:
                    self.vel.rotate_ip_rad(2 * y + 2 * a)
                print(a, block.angle, block.angle % (2 * math.pi))

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
