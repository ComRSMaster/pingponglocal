from typing import Callable

import pygame
from pygame import Vector2

HOVERED_COLOR = (220, 220, 220)
PRESSED_COLOR = (180, 180, 180)
NORMAL_COLOR = (255, 255, 255)
LERP_SPEED = .1


def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1


def lerp_color(color1, color2):
    return [lerp(v0, v1, LERP_SPEED) for v0, v1 in zip(color1, color2)]


class Button:
    class State:
        NORMAL = 0
        HOVERED = 1
        PRESSED = 2

    def __init__(self, text: str, center: Vector2, on_click: Callable, color: tuple[int, int, int] = NORMAL_COLOR):
        self.text = text
        self.width = 250
        self.height = 80
        self.center = center
        self.rect = pygame.Rect(center[0] - self.width / 2, center[1] - self.height / 2, self.width, self.height)
        self.color = color
        self.on_click = on_click

        self.font = pygame.font.SysFont('arial', 42)
        self.rendered_text = self.font.render(self.text, True, 'black')
        self.state = Button.State.NORMAL
        self.is_pressed = False

    def render(self, screen: pygame.Surface, mouse_pos: tuple[int, int]):
        self.process_mouse(mouse_pos)

        if self.state == Button.State.NORMAL:
            self.color = lerp_color(self.color, NORMAL_COLOR)
        elif self.state == Button.State.HOVERED:
            self.color = lerp_color(self.color, HOVERED_COLOR)
        elif self.state == Button.State.PRESSED:
            self.color = lerp_color(self.color, PRESSED_COLOR)

        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.rendered_text, self.center - self.rendered_text.get_rect().center)

    def process_mouse(self, pos: tuple[int, int]):
        if self.rect.collidepoint(pos):
            if self.state != Button.State.PRESSED:
                self.state = Button.State.HOVERED
        else:
            self.state = Button.State.NORMAL

    def on_mousedown(self, pos: tuple[int, int]):
        if self.rect.collidepoint(pos):
            print('on_mousedown')
            self.state = Button.State.PRESSED

    def on_mouseup(self, pos: tuple[int, int]):
        if self.rect.collidepoint(pos):
            print('on_mouseup')
            self.state = Button.State.HOVERED
            self.on_click()
        else:
            self.state = Button.State.NORMAL


class UI:
    def __init__(self, buttons: list[Button]):
        self.buttons = buttons

    def render(self, screen: pygame.Surface):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.render(screen, mouse_pos)

    def on_mousedown(self, pos: tuple[int, int]):
        for button in self.buttons:
            button.on_mousedown(pos)

    def on_mouseup(self, pos: tuple[int, int]):
        for button in self.buttons:
            button.on_mouseup(pos)
