import pygame

class Block:

    def __init__(self, posx, posy, width, height):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

    def draw(self, Display):
        pygame.draw.rect(Display, [6,130,183], [self.posx, self.posy, self.width, self.height])

    def move(self, mouseX):
        self.posx = mouseX - self.width / 2