import sys
import pygame
import random

from pygame import mixer

from paddle import Paddle
from ball import Ball

print(sys.version_info)

def pong():
    #INIT
    pygame.init()

    paddleSound = pygame.mixer.Sound('C:\\Users\\cqwhi\\PycharmProjects\\Pong\\venv\\pongblip.wav')
   # pongMusic = pygame.mixer.music.load('C:\\Users\\cqwhi\\PycharmProjects\\Pong\\venv\\ambient-piano-mix.wav')

    clock = pygame.time.Clock()

    menuState = True
    winState = False
    aiState = False

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

    p1Score=0
    p2Score=0


    done=False
    #Game Loop
    while not done:
        #Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        if menuState == True:
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_e]):
                menuState=False
            if (keys[pygame.K_ESCAPE]):
                done = True
            if (keys[pygame.K_f]):
                menuState = False
                aiState = True
            surf.fill((BLACK))
            font = pygame.font.Font(None, 50)
            text = font.render("Press E to play PyPong! 2 Player", 10, WHITE)
            surf.blit(text, (75, 150))
            text2 = font.render("Press F to play PyPong! 1 Player", 10, WHITE)
            surf.blit(text2, (75, 250))
            pygame.display.update()
        elif winState == True:
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_e]):
                winState = False
            if (keys[pygame.K_ESCAPE]):
                done = True
            surf.fill((BLACK))
            font = pygame.font.Font(None, 50)
            winText = font.render(winner+" Wins!", 10, WHITE)
            surf.blit(winText, (150, 100))
            text = font.render("Press E to play again!", 10, WHITE)
            surf.blit(text, (150, 200))
            #reset the board
            p1Score=0
            p2Score=0
            player1.rect.x = 20
            player1.rect.y = 200
            player2.rect.x = 670
            player2.rect.y = 200
            pygame.display.update()
        else:
            keys = pygame.key.get_pressed()
            if(keys[pygame.K_w]):
                player1.up(5)
            if (keys[pygame.K_s]):
                player1.down(5)
            if (keys[pygame.K_UP] and aiState == False):
                player2.up(5)
            if (keys[pygame.K_DOWN] and aiState == False):
                player2.down(5)
            if(keys[pygame.K_ESCAPE]):
                done=True

            if aiState == True:
                if(ball.rect.y < player2.rect.y):
                    player2.up(3)
                elif (ball.rect.y > player2.rect.y):
                    player2.down(3)

            #Game logic/update
            spiritGroup.update()

            if ball.rect.x >= 690:
                p1Score += 1
                ball.rect.x = 345
                ball.rect.y = 195
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0:
                p2Score += 1
                ball.rect.x = 345
                ball.rect.y = 195
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y > screenHeight:
                paddleSound.play()
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y < 0:
                paddleSound.play()
                ball.velocity[1] = -ball.velocity[1]

            if pygame.sprite.collide_mask(ball, player1) or pygame.sprite.collide_mask(ball,player2):
                paddleSound.play()
                ball.bounce()
                #Game Draw
            surf.fill((BLACK))
            pygame.draw.line(surf, WHITE, [349, 0], [349, 500], 5)
            spiritGroup.draw(surf)

            font = pygame.font.Font(None, 74)
            text = font.render(str(p1Score), 1, WHITE)
            surf.blit(text, (250, 10))
            text = font.render(str(p2Score), 1, WHITE)
            surf.blit(text, (420, 10))

            if(p1Score >=2):
                winState = True
                winner="Player 1"
            elif (p2Score >= 2):
                winState = True
                winner = "Player 2"

            pygame.display.update()

            clock.tick(30)
    pygame.quit()