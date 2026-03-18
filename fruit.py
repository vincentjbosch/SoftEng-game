BLACK = (0, 0, 0)

class Fruit:
    def __init__(self):
        self.block = (10, 8)

    def draw(self):
        self.screen.fill(BLACK)
        self.draw.circle()