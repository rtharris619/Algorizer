import math


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192),
    ]

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, game, width, height, lst):

        self.FONT = game.font.SysFont('comicsans', 20)
        self.LARGE_FONT = game.font.SysFont('comicsans', 30)

        self.width = width
        self.height = height
        self.lst = lst
        self.min_val = 0
        self.max_val = 0
        self.block_width = 0
        self.block_height = 0
        self.start_x = 0
        self.start_y = 0

        self.window = game.display.set_mode((width, height))
        game.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = math.floor((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
