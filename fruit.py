import pygame, random

from player import Player

RED = (100, 0, 0)

class Fruit:
    def __init__(self, screen, block_size):
        self.screen = screen
        self.radius = block_size//2
        self.pos = (10, 8)
        self.block_size = block_size        

    def draw(self):
        middle = (self.pos[0] * self.block_size + self.radius, self.pos[1] * self.block_size + self.radius)
        pygame.draw.circle(self.screen, RED, middle, self.radius)

    def get(self, snake):
        free = []
        for i in range(4):
            for j in range(4):
                if (i,j) not in snake.slang:
                    free.append((i, j))
        
        self.pos = random.choice(free)
        #player.score += 1
        


