import pygame

from constants import SIZE, FPS
from game import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    game = Game()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     ui.get_click(event.pos)

        screen.fill((0, 0, 0))

        game.process_keys(pygame.key.get_pressed())
        game.render(screen)

        # обновление экрана
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
