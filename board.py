import pygame

BLACK = (0,0,0)
YELLOW = (255, 220, 85)
ORANGE = (255, 200, 40)

class Board:
    """ Represents the playing field of the game. """
    def __init__(self, screen, block_amount, block_size):
        """
        Initialize the board.

        Args:
            screen (pygame.Surface): Surface to draw on.
            block_amount (int): Amount of blocks across the grid.
            block_size (int): Size of each cell in pixels.
        """
        self.block_amount = block_amount
        self.screen = screen
        self.block_size = block_size
    
    def draw(self):
        """ Draw the grid background. """
        self.screen.fill(BLACK)
        for i in range(self.block_amount):
            for j in range(self.block_amount):
                rect = pygame.Rect(self.block_size * i, self.block_size * j, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, YELLOW, rect)
                pygame.draw.rect(self.screen, ORANGE, rect, 1)