import pygame
from pygame import Vector2

from constants import WIDTH, HEIGHT, FPS


class Block:
    SPEED = 3.5 / FPS
    PADDING = 50
    MOVE_RADIUS = min(WIDTH / 2, HEIGHT / 2) - PADDING
    CENTER = Vector2(WIDTH / 2, HEIGHT / 2)
    BLOCK_WIDTH = 0.5
    BLOCK_HEIGHT = 5

    # MAX_X = WIDTH - PADDING
    # MIN_X = PADDING

    def __init__(self):
        self.angle = -2

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (50, 50, 50), self.CENTER, self.MOVE_RADIUS)

        pygame.draw.arc(screen, (0, 255, 0),
                        (WIDTH / 2 - self.MOVE_RADIUS, HEIGHT / 2 - self.MOVE_RADIUS,
                         self.MOVE_RADIUS * 2, self.MOVE_RADIUS * 2),
                        self.angle - self.BLOCK_WIDTH, self.angle + self.BLOCK_WIDTH, self.BLOCK_HEIGHT)

    def delta_move(self, delta):
        self.angle += delta * self.SPEED
