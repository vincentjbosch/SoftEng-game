import pygame
from snake_abstract import Snake_Abstract

PURPLE = (167, 88, 162)
DARKER_PURPLE = (137, 41, 133)

class Player(Snake_Abstract):
    """ Player controlled snake. """
    def __init__(self):
        """Initialize the player snake."""
        self.slang = [(5, 5), (4, 5), (3, 5)]
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.color = PURPLE
        self.head_color = DARKER_PURPLE

    def move(self, fruit):
        """
        Move the snake forward and handle fruit consumption.

        Args:
            fruit (Fruit): Fruit object.
        """
        head_x, head_y = self.slang[0]
        self.direction = self.next_direction

        if self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)

        self.slang.insert(0, new_head)
        
        if self.slang[0] == fruit.pos:
            fruit.respawn(self)
        else:     
            self.slang.pop()
    
    def wall_collision(self, block_amount):
        """
        Check collision with walls.

        Args:
            block_amount (int): Amount of blocks across the grid.

        Returns:
            bool: True if collision occurs.
        """
        head_x, head_y = self.slang[0]
        
        if head_x < 0 or head_x >= block_amount:
            return True
        
        if head_y < 0 or head_y >= block_amount:
            return True
        
        return False