import pygame

from board import Board
from player import Player
from fruit import Fruit

def main():
    pygame.init()
    width, height = 500, 500
    block_amount = 16
    block_size = min(width, height)//block_amount

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake = Player()
    board = Board(screen, block_amount, block_size)
    fruit = Fruit(screen, block_size)

    running = True
    while running:
        clock.tick(4)
        board.draw()
        snake.draw(screen, block_size)
        fruit.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
                elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"

        snake.move(fruit)

        if snake.wall_collision(block_amount):
            running = False        

    pygame.quit()

if __name__ == '__main__':
    main()