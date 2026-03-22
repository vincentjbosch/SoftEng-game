import pygame, random

from snake_abstract import Snake_Abstract

RED = (200, 0, 0)
DARKER_RED = (150, 0, 0)


class Enemy(Snake_Abstract):
    def __init__(self):
        self.slang = [(7, 10), (6, 10), (5, 10)]
        self.color = RED
        self.head_color = DARKER_RED

    def move(self, block_amount):
        head_x, head_y = self.slang[0]

        direction = random.choice(["RIGHT", "LEFT", "UP", "DOWN"])

        if direction == "RIGHT":
            head_x += 1
        elif direction == "LEFT":
            head_x -= 1
        elif direction == "UP":
            head_y -= 1
        elif direction == "DOWN":
            head_y += 1

        head_x %= block_amount
        head_y %= block_amount
        new_head = (head_x, head_y)

        self.slang.insert(0, new_head)
        self.slang.pop()

