import pygame

PURPLE = (167, 88, 162)
DARKER_PURPLE = (137, 41, 133)

class Player():
    def __init__(self):
        self.slang = [(5, 5), (4, 5), (3, 5)]
       
    def draw(self, screen, block_size):
        for i, (x, y) in enumerate(self.slang):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            color = DARKER_PURPLE if i == 0 else PURPLE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, DARKER_PURPLE, rect, 1)



