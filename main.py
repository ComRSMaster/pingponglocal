import pygame

from constants import SIZE, FPS
from screenmanager import ScreenManager
from screens.game import Game
from screens.ipselector import IPSelector


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    ScreenManager.change_screen(Game())
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ScreenManager.current_screen.ui.on_mousedown(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                ScreenManager.current_screen.ui.on_mouseup(event.pos)

        screen.fill((0, 0, 0))

        ScreenManager.current_screen.process_keys(pygame.key.get_pressed())
        ScreenManager.current_screen.render(screen)
        ScreenManager.current_screen.ui.render(screen)

        # обновление экрана
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
