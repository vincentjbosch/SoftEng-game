import pygame
import time

BLACK = (0,0,0)
YELLOW = (255, 220, 85)
ORANGE = (255, 200, 40)

BLOCK_AMOUNT = 16

class Board:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake")
        self.block_size = min(width, height)//BLOCK_AMOUNT
    
    def draw(self):
        self.screen.fill(BLACK)
        for i in range(BLOCK_AMOUNT):
            for j in range(BLOCK_AMOUNT):
                rect = pygame.Rect(self.block_size * i, self.block_size * j, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, YELLOW, rect)
                pygame.draw.rect(self.screen, ORANGE, rect, 1)
        pygame.display.update()


    

        
