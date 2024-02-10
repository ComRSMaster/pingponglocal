import pygame

from constants import WIDTH, HEIGHT


class Block:
    SPEED = 0.03
    PADDING = 50
    MOVE_RADIUS = min(WIDTH / 2, HEIGHT / 2) - PADDING
    BLOCK_WIDTH = 0.2
    BLOCK_HEIGHT = 20

    # MAX_X = WIDTH - PADDING
    # MIN_X = PADDING

    def __init__(self):
        self.angle = 0

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, (50, 50, 50), (WIDTH / 2, HEIGHT / 2),
                           self.MOVE_RADIUS)

        pygame.draw.arc(screen, (0, 255, 0),
                        (WIDTH / 2 - self.MOVE_RADIUS, HEIGHT / 2 - self.MOVE_RADIUS,
                         self.MOVE_RADIUS * 2, self.MOVE_RADIUS * 2),
                        self.angle - self.BLOCK_WIDTH, self.angle + self.BLOCK_WIDTH, self.BLOCK_HEIGHT)

    def delta_move(self, delta):
        self.angle += delta * self.SPEED
