import pygame
import sys
import block
import paddle
import ball

import random

width = 800
height = 600
backgroundColor = [255,223,125]
FPS = 60
n = 10
blockWidth = width // n
blockHeight = blockWidth / 2

paddleWidth = 200
paddleHeight = 30
paddleX = width / 2 - (paddleWidth / 2)
paddleY = height - paddleHeight - 10

ballRadius = 15

# Draw paddle and ball
user = paddle.Paddle(paddleX, paddleY, paddleWidth, paddleHeight)
ball = ball.Ball(int(width / 2), int(height/2), ballRadius)

# Function to exit game
def gameOver():
    pygame.quit()
    sys.exit()

# create array of blocks
blocks = []

# Allows blocks to be separated by the offset so that blocks can be individually identified
offset = 10
for y in range(3):
    offset += 5
    for x in range(0, width, blockWidth + 10):

        blocks.append(block.Block(x, blockHeight * (y+1) + offset, blockWidth, blockHeight))

# Sets graphical components of display window
pygame.init()
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
        ball.draw(window)
        user.draw(window)
        user.move(pygame.mouse.get_pos()[0])
        #window.display.flip()
        for i in range(len(blocks)):
            blocks[i].draw(window)
        pygame.display.update()
        FPSClock.tick(FPS)

fps = pygame.time.Clock()
