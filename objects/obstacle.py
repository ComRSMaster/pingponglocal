import pygame
from pygame import Vector2


class Obstacle(pygame.sprite.Sprite):
    width = 40
    height = 30

    def __init__(self,
                 position: Vector2,
                 group: pygame.sprite.Group):
        super().__init__()
        self.image = None
        self.rect = pygame.Rect(position.x - self.width // 2, position.y - self.height // 2, self.width, self.height)
        self.group = group
        self.add(group)

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (200, 0, 0), self.rect)
