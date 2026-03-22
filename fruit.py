import pygame, random

from player import Player

RED = (100, 0, 0)

class Fruit:
    """ Represents a fruit that the snake can eat. """
    def __init__(self, screen, block_size, block_amount):
        """
        Initialize the fruit.

        Args:
            screen (pygame.Surface): Surface to draw on.
            block_size (int): Size of one grid cell in pixels.
            block_amount (int): Amount of blocks across the grid.
        """
        self.screen = screen
        self.radius = block_size//2
        self.pos = (10, 8)
        self.block_size = block_size    
        self.block_amount = block_amount    

    def draw(self):
        """ Draw the fruit on the screen. """
        middle = (self.pos[0] * self.block_size + self.radius, self.pos[1] * self.block_size + self.radius)
        pygame.draw.circle(self.screen, RED, middle, self.radius)

    def respawn(self, snake):
        """
        Place the fruit on a random free position.

        Args:
            snake (Snake_Abstract): Snake object to avoid collisions with.
        """
        free = []
        for i in range(self.block_amount):
            for j in range(self.block_amount):
                if (i,j) not in snake.slang:
                    free.append((i, j))
        
        self.pos = random.choice(free)