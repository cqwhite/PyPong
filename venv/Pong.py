import sys
import pygame
import random

print(sys.version_info)

def pong():
    #INIT
    pygame.init()

    clock = pygame.time.Clock()

    BLACK = (0,0,0)
    WHITE = (255,255,255)

    screenWidth=700
    screenHeight=700

    surf=pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption("PyPong!")

    done=False
    #Game Loop
    while not done:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        #Game logic/update

        #Game Draw
        surf.fill((BLACK))
        pygame.draw.line(surf, WHITE, [349, 0], [349, 500], 5)
        pygame.display.flip()
        pygame.display.update()

        clock.tick(30)
    pygame.quit()