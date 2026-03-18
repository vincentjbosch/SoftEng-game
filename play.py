import pygame
import time

from board import Board
from player import Player

def main():
    pygame.init()
    width, height = 800, 500
    block_amount = 16
    block_size = min(width, height)//block_amount

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")

    snake = Player()
    board = Board(screen, block_amount, block_size)

    running = True
    while running:
        board.draw()
        snake.draw(screen, block_size)
        time.sleep(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    main()