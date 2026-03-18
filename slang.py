import pygame
import time

from board import Board

def main():
    pygame.init()
    board = Board(500, 500)
    while True:
        board.draw()
        time.sleep(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == '__main__':
    main()