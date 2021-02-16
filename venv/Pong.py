import sys
import pygame
import random

from paddle import Paddle
from ball import Ball

print(sys.version_info)

def pong():
    #INIT
    pygame.init()

    clock = pygame.time.Clock()

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (199, 0, 57)
    BLUE = (44, 150, 239)

    screenWidth=700
    screenHeight=500

    surf=pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption("PyPong!")

    player1 = Paddle(RED, 10, 100)
    player1.rect.x=20
    player1.rect.y=200

    player2 = Paddle(BLUE, 10, 100)
    player2.rect.x=670
    player2.rect.y=200

    ball = Ball(WHITE,10,10)
    ball.rect.x = 345
    ball.rect.y = 195

    spiritGroup = pygame.sprite.Group()
    spiritGroup.add(player1)
    spiritGroup.add(player2)
    spiritGroup.add(ball)



    done=False
    #Game Loop
    while not done:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            player1.up(5)
        if (keys[pygame.K_s]):
            player1.down(5)
        if (keys[pygame.K_UP]):
            player2.up(5)
        if (keys[pygame.K_DOWN]):
            player2.down(5)
        if(keys[pygame.K_ESCAPE]):
            done=True

        #Game logic/update
        spiritGroup.update()

        if ball.rect.x >= screenWidth:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > screenHeight:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, player1) or pygame.sprite.collide_mask(ball,player2):
            ball.bounce()
            #Game Draw
        surf.fill((BLACK))
        pygame.draw.line(surf, WHITE, [349, 0], [349, 500], 5)
        spiritGroup.draw(surf)
        pygame.display.update()

        clock.tick(30)
    pygame.quit()