import pygame, random

from player import Player

RED = (100, 0, 0)

class Fruit:
    def __init__(self, screen, block_size, block_amount):
        self.screen = screen
        self.radius = block_size//2
        self.pos = (10, 8)
        self.block_size = block_size    
        self.block_amount = block_amount    

    def draw(self):
        middle = (self.pos[0] * self.block_size + self.radius, self.pos[1] * self.block_size + self.radius)
        pygame.draw.circle(self.screen, RED, middle, self.radius)

    def get(self, snake):
        free = []
        for i in range(self.block_amount):
            for j in range(self.block_amount):
                if (i,j) not in snake.slang:
                    free.append((i, j))
        
        self.pos = random.choice(free)

        


