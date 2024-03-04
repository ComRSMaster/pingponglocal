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


class Selectable:
    class State:
        NORMAL = 0
        HOVERED = 1
        PRESSED = 2

    def __init__(self,
                 center: Vector2,
                 size: tuple[int, int],
                 color: tuple[int, int, int] = NORMAL_COLOR):
        self.width = size[0]
        self.height = size[1]
        self.center = center
        self.rect = pygame.Rect(center[0] - self.width / 2, center[1] - self.height / 2, self.width, self.height)
        self.color = color

        self.state = Button.State.NORMAL
        self.selected = False

    def base_render(self, screen: pygame.Surface, mouse_pos: tuple[int, int]):
        self.process_mouse(mouse_pos)

        if self.state == Button.State.NORMAL:
            self.color = lerp_color(self.color, NORMAL_COLOR)
        elif self.state == Button.State.HOVERED:
            self.color = lerp_color(self.color, HOVERED_COLOR)
        elif self.state == Button.State.PRESSED:
            self.color = lerp_color(self.color, PRESSED_COLOR)

        pygame.draw.rect(screen, self.color, self.rect)

        self.render(screen)

    def process_mouse(self, pos: tuple[int, int]):
        if self.rect.collidepoint(pos):
            if self.state != Button.State.PRESSED:
                self.state = Button.State.HOVERED
        else:
            self.state = Button.State.NORMAL

    def global_mousedown(self, pos: tuple[int, int]):
        if self.rect.collidepoint(pos):
            # print('on_mousedown')
            self.selected = True
            self.state = Button.State.PRESSED
            self.on_mousedown()
        else:
            self.selected = False

    def global_mouseup(self, pos: tuple[int, int]):
        if self.rect.collidepoint(pos):
            # print('on_mouseup')
            self.state = Button.State.HOVERED
            self.on_click()
        else:
            self.state = Button.State.NORMAL

    def on_mousedown(self):
        pass

    def on_click(self):
        pass

    def render(self, screen: pygame.Surface):
        pass


class Button(Selectable):
    def __init__(self,
                 text: str,
                 center: Vector2,
                 size: tuple[int, int],
                 on_click: Callable,
                 color: tuple[int, int, int] = NORMAL_COLOR):
        super().__init__(center, size, color)
        self.text = text
        self.on_click = on_click

        self.font = pygame.font.SysFont('Noto Sans Black', 56)
        self.rendered_text = self.font.render(self.text, True, 'black')

    def render(self, screen: pygame.Surface):
        screen.blit(self.rendered_text, self.center - self.rendered_text.get_rect().center)


class TextInput(Selectable):
    def __init__(self,
                 placeholder: str,
                 center: Vector2,
                 size: tuple[int, int],
                 color: tuple[int, int, int] = NORMAL_COLOR):
        super().__init__(center, size, color)
        self.rendered_text = None
        self.text = ''
        self.placeholder = placeholder

        self.font = pygame.font.SysFont('Noto Sans Black', 56)
        self.rendered_placeholder = self.font.render(self.placeholder, True, '#999999')

    def render(self, screen: pygame.Surface):
        screen.blit(self.rendered_text if self.text else self.rendered_placeholder,
                    self.center - (self.width // 2 - 30, self.rendered_placeholder.get_height() // 2))

    def set_text(self, text: str):
        self.text = text
        self.rendered_text = self.font.render(self.text, True, 'black')

    def get_text(self):
        return self.text


class TextView:
    rendered_text: pygame.Surface

    def __init__(self,
                 text: str,
                 center: Vector2):
        self.text = None
        self.center = center
        self.font = pygame.font.SysFont('Noto Sans Black', 56)

        self.set_text(text)

    def base_render(self, screen: pygame.Surface, mouse_pos: tuple[int, int]):
        screen.blit(self.rendered_text, self.center - self.rendered_text.get_rect().center)

    def set_text(self, text: str):
        self.text = text
        self.rendered_text = self.font.render(self.text, True, 'white')

    def get_text(self):
        return self.text

    def global_mousedown(self, pos: tuple[int, int]):
        pass

    def global_mouseup(self, pos: tuple[int, int]):
        pass


class UI:
    def __init__(self, buttons: list):
        self.buttons = buttons

    def render(self, screen: pygame.Surface):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.base_render(screen, mouse_pos)

    def on_mousedown(self, pos: tuple[int, int]):
        for button in self.buttons:
            button.global_mousedown(pos)

    def on_mouseup(self, pos: tuple[int, int]):
        for button in self.buttons:
            button.global_mouseup(pos)
