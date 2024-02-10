
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

