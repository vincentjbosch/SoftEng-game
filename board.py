import pygame
import time

BLACK = (0,0,0)
GREEN = (0, 200, 0)

BLOCK_AMOUNT = 16

class Board:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake")
        self.block_size = width//BLOCK_AMOUNT
        self.clock = pygame.time.Clock()
    
    def draw(self):
        self.screen.fill(BLACK)
        for i in range(BLOCK_AMOUNT):
            for j in range(BLOCK_AMOUNT):
                rect = pygame.Rect(self.block_size * i, self.block_size * j, self.block_size, self.block_size)
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    board = Board(500, 500)
    while True:
        board.draw()
        time.sleep(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


    

        
