from abc import ABC, abstractmethod
import pygame

class Snake_Abstract(ABC):
    """ Abstract class for a snake. """
    @abstractmethod
    def __init__(self):
        """ Initialize the snake. """
        ...

    def change_direction(self, new_direction):
        """ Changes the direction of the snake. """
        opposite_directions = {
            "RIGHT" : "LEFT",
            "LEFT" : "RIGHT",
            "UP" : "DOWN",
            "DOWN" : "UP"
        }

        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction

    def draw(self, screen, block_size):
        """ Draws the snake on the screen. """
        for i, (x, y) in enumerate(self.slang):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            if i == 0:
                pygame.draw.rect(screen, self.color, rect)
                pygame.draw.rect(screen, self.head_color, rect, 1)
            else:
                pygame.draw.rect(screen, self.color, rect)

    def self_collision(self):
        head = self.slang[0]
        return head in self.slang[1:]

    @abstractmethod
    def move(self, fruit):
        """ Moves the snake. """
    
    @abstractmethod
    def wall_collision(self, block_amount):
        """ Handles wall collision """

