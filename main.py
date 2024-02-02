import pygame

SIZE = WIDTH, HEIGHT = 1200, 800
FPS = 60


class Block:
    SPEED = 8
    PADDING = 50
    MAX_X = WIDTH - PADDING
    MIN_X = PADDING

    def __init__(self):
        self.width = 200
        self.height = 30
        self.x = 50
        self.y = 50

    def render(self, screen: pygame.Surface):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, 'white', rect)
    #
    # def move(self, new_x, new_y):
    #     self.x = new_x
    #     self.y = new_y

    # def delta_move(self, delta_x, delta_y):
    #     self.x = min(max(self.x + delta_x, self.MIN_X), self.MAX_X)
    #     self.y = min(max(self.y + delta_y, 0), HEIGHT)
    def delta_move(self, delta):
        self.x = min(max(self.x + delta * self.SPEED, self.MIN_X), self.MAX_X - self.width)


class Ball:
    def __init__(self):
        self.radius = 15
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

    def render(self, screen: pygame.Surface):
        pygame.draw.circle(screen, 'white', (self.x, self.y), self.radius)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def delta_move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class Game:
    def __init__(self):
        self.block = Block()
        self.ball = Ball()

    def render(self, screen: pygame.Surface):
        self.ball.render(screen)
        self.block.render(screen)

    def process_keys(self, keys):
        if keys[pygame.K_LEFT]:
            self.block.delta_move(-1)
        if keys[pygame.K_RIGHT]:
            self.block.delta_move(1)


# class UI:
#     def __init__(self):
#         pass
#
#     def render(self, screen: pygame.Surface):
#         pass
#         # for y in range(self.height):
#
#     def on_click(self, cell_coords: tuple[int, int]):
#         print(cell_coords)
#         if cell_coords is not None:
#             for x in range(self.width):
#                 self.board[cell_coords[1]][x] = not self.board[cell_coords[1]][x]
#             for y in range(self.height):
#                 if y == cell_coords[1]:
#                     continue
#                 self.board[y][cell_coords[0]] = not self.board[y][cell_coords[0]]
#             print(self.board)
#
#     def get_click(self, mouse_pos: tuple[int, int]):
#         self.on_click(self.get_cell(mouse_pos))


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
