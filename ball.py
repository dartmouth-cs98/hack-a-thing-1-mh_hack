import pygame

class Ball:

    def __init__(self, posX, posY, radius):
        self.posX = posX
        self.posY = posY
        self.radius = radius

    def draw(self, Display):
        pygame.draw.circle(Display,[208,16,16], (self.posX,self.posY), 20)