import pygame

from board import Board
from player import Player
from fruit import Fruit
from enemy import Enemy

WHITE = (255, 255, 255)

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, WHITE)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)

def reset_game(screen, block_amount, block_size, enemy_bool):
    snake = Player()
    if enemy_bool:
        enemy = Enemy()
    else:
        enemy = None
    board = Board(screen, block_amount, block_size)
    fruit = Fruit(screen, block_size, block_amount)
    fruit.get(snake)
    return snake, enemy, board, fruit

def main():
    pygame.init()

    width, height = 500, 500
    block_amount = 17
    block_size = min(width, height) // block_amount

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    running = True
    enemy_bool = True
    game_state = "HOME"

    snake, enemy, board, fruit = reset_game(screen, block_amount, block_size, enemy_bool)


    while running:
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_state == "HOME":
                    if event.key == pygame.K_SPACE:
                        snake, enemy, board, fruit = reset_game(screen, block_amount, block_size, enemy_bool)
                        game_state = "PLAYING"
                    if event.key == pygame.K_e:
                        enemy_bool = not enemy_bool

                elif game_state == "PLAYING":
                    if event.key == pygame.K_RIGHT:
                        snake.change_direction("RIGHT")
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction("LEFT")
                    elif event.key == pygame.K_UP:
                        snake.change_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction("DOWN")

                elif game_state == "GAME_OVER":
                    if event.key == pygame.K_r:
                        snake, enemy, board, fruit = reset_game(screen, block_amount, block_size, enemy_bool)
                        game_state = "PLAYING"
                    elif event.key == pygame.K_h:
                        game_state = "HOME"

        board.draw()

        if game_state == "HOME":
            draw_text(screen, "SNAKE", 60, width // 2, height // 2 - 60)
            draw_text(screen, "Druk op SPACE om te starten", 28, width // 2, height // 2)
            draw_text(screen, "Druk op E om enemy aan/uit te zetten", 28, width // 2, height // 2 + 40)
            if enemy_bool:
                draw_text(screen, "Enemy: AAN", 28, width // 2, height // 2 + 80)
            else:
                draw_text(screen, "Enemy: UIT", 28, width // 2, height // 2 + 80)
            draw_text(screen, "Gebruik de pijltjestoetsen om te bewegen", 24, width // 2, height // 2 + 120)

        elif game_state == "PLAYING":
            snake.move(fruit)
            if enemy_bool:
                enemy.move(block_amount)

            if snake.wall_collision(block_amount) or snake.self_collision():
                game_state = "GAME_OVER"
            
            if enemy_bool and snake.enemy_collision(enemy):
                game_state = "GAME_OVER"

            fruit.draw()
            snake.draw(screen, block_size)
            if enemy_bool:
                enemy.draw(screen, block_size)

            score = len(snake.slang) - 3
            draw_text(screen, f"Score: {score}", 30, width // 2, 20)

        elif game_state == "GAME_OVER":
            fruit.draw()
            snake.draw(screen, block_size)
            if enemy_bool:
                enemy.draw(screen, block_size)

            score = len(snake.slang) - 3
            draw_text(screen, "GAME OVER", 55, width // 2, height // 2 - 50)
            draw_text(screen, f"Score: {score}", 30, width // 2, height // 2)
            draw_text(screen, "Druk op R om opnieuw te spelen", 26, width // 2, height // 2 + 40)
            draw_text(screen, "Druk op H voor homescreen", 26, width // 2, height // 2 + 75)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()  