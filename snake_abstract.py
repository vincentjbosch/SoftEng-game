from abc import ABC, abstractmethod
import pygame

class Snake_Abstract(ABC):
    """ Abstract base class for snake entities. """
    @abstractmethod
    def __init__(self):
        """ Initialize the snake. """
        ...

    def change_direction(self, new_direction):
        """ Changes the direction of the snake if it's not directly opposite.

        Args:
            new_direction (str): One of ('UP', 'DOWN', 'LEFT', 'RIGHT')
        """
        opposite_directions = {
            "RIGHT" : "LEFT",
            "LEFT" : "RIGHT",
            "UP" : "DOWN",
            "DOWN" : "UP"
        }

        if new_direction != opposite_directions[self.direction]:
            self.next_direction = new_direction

    def draw(self, screen, block_size):
        """
        Draw the snake on the screen.

        Args:
            screen (pygame.Surface): Surface to draw on.
            block_size (int): Size of one grid cell.
        """
        for i, (x, y) in enumerate(self.slang):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            if i == 0:
                pygame.draw.rect(screen, self.color, rect)
                pygame.draw.rect(screen, self.head_color, rect, 1)
            else:
                pygame.draw.rect(screen, self.color, rect)

    def self_collision(self):
        """
        Check if the snake collides with itself.

        Returns:
            bool: True if collision occurs.
        """
        head = self.slang[0]
        return head in self.slang[1:]
    
    def enemy_collision(self, enemy):
        """
        Check collision with another snake.

        Args:
            enemy (SnakeAbstract): Another snake.

        Returns:
            bool: True if any segment overlaps.
        """
        for pos in self.slang:
            if pos in enemy.slang:
                return True
        return False

    @abstractmethod
    def move(self, fruit):
        """ Move the snake. """