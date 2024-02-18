class _ScreenManager:
    def __init__(self):
        self.current_screen = None

    def change_screen(self, new_screen):
        self.current_screen = new_screen


ScreenManager = _ScreenManager()
