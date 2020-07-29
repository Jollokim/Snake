import pygame
import snake as sn
import random

class Apple:
    def __init__(self, win, snake):
        self.win = win
        self.snake = snake
        self.applePos = self.nextApplePos()

    def nextApplePos(self):
        snx = self.snake.snakeX
        sny = self.snake.snakeY
        avalpos = []

        for xpos in range(0, 480, 20):
            for ypos in range(0, 480, 20):
                for i in range(len(snx)):
                    if snx[i]+20 > xpos and xpos+20 > snx[i] and sny[i]+20 > ypos and ypos+20 > sny[i]:
                        break
                    if i == len(snx)-1:
                        avalpos.append((xpos, ypos))




        if len(avalpos) == 0:
            self.snake.victory = True
            return


        randompos = random.randrange(len(avalpos))

        print(avalpos[randompos])

        return avalpos[randompos]

    def chechHit(self):
        snx = self.snake.snakeX[0]
        sny = self.snake.snakeY[0]

        xpos = self.applePos[0]
        ypos = self.applePos[1]




        if (snx > xpos-sn.Snake.dim and snx < xpos+sn.Snake.dim) and (sny > ypos-sn.Snake.dim and sny < ypos+sn.Snake.dim):
            print(snx, sny)

            print(xpos, ypos)

            print("snake grows")
            self.snake.appleEaten += 1

            self.applePos = self.nextApplePos()
            self.snake.snakeGrow()


    def render(self):

        if self.snake.snakeAlive:
            self.chechHit()

        pygame.draw.rect(self.win, (255, 0, 0), (self.applePos[0], self.applePos[1], sn.Snake.dim, sn.Snake.dim))





