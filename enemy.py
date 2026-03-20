import pygame, random

from snake_abstract import Snake_Abstract

RED = (200, 0, 0)
DARKER_RED = (150, 0, 0)


class Enemy(Snake_Abstract):
    def __init__(self):
        self.slang = [(7, 7), (6, 7), (5, 7)]
        self.color = RED
        self.head_color = DARKER_RED

    def move(self):
        head_x, head_y = self.slang[0]

        direction = random.choice(["RIGHT", "LEFT", "UP", "DOWN"])

        if direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        elif direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif direction == "UP":
            new_head = (head_x, head_y - 1)
        elif direction == "DOWN":
            new_head = (head_x, head_y + 1)

        self.slang.insert(0, new_head)
        self.slang.pop()

    def wall_collision(self, block_amount):
        head_x, head_y = self.slang[0]
        
        if head_x < 0:
            head_x = block_amount

        if head_x >= block_amount:
            head_x = 0
        
        if head_y < 0:
            head_y = block_amount
        
        if head_y >= block_amount:
            head_y = 0
