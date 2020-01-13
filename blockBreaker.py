import pygame
import sys
import block
import random

width = 800
height = 600
backgroundColor = [255,223,125]
FPS = 60
n = 10
blockWidth = width // n
blockHeight = blockWidth / 2

pygame.init()

def gameOver():
    pygame.quit()
    sys.exit()

blocks = []

for x in range(0, width, blockWidth + 10):
    blocks.append(block.Block(x, 50, blockWidth, blockHeight))

pygame.display.set_caption("Blockbreaker")
window = pygame.display.set_mode([width, height])
window.fill(backgroundColor)

FPSClock = pygame.time.Clock()
FPS = 60

gameOver = False
print(len(blocks))

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        window.fill(backgroundColor)
        #window.display.flip()
        for i in range(len(blocks)):
            blocks[i].draw(window)
        pygame.display.update()
        FPSClock.tick(FPS)

fps = pygame.time.Clock()
