import pygame

class Snake:
    dim = 20
    vel = 5
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    STARTX = 240
    STARTY = 240


    def __init__(self, win):
        self.snakeX = []
        self.snakeY = []
        self.snakeDirection = []
        for i in range(5):
            self.snakeX.append(Snake.STARTX)
            self.snakeY.append(Snake.STARTY + (25*i))
            self.snakeDirection.append(Snake.UP)
        self.currentLength = len(self.snakeX)
        self.snakeCorner = []
        self.snakeMove = True
        self.snakeAlive = True
        self.re_to_cha_Dir = True
        self.win = win
        self.lastWait = 6
        self.lastDirection = None
        self.waitTails = 0
        self.growthRate = 2
        self.victory = False
        self.appleEaten = 0
        self.cheatCode = [0, 0, 0]


    def _forward(self):

        for i in range(len(self.snakeX)):

            for ci in range(len(self.snakeCorner)):
               # when snake part passes corner
               if self.snakeY[i] == self.snakeCorner[ci][1] and self.snakeX[i] == self.snakeCorner[ci][0]:
                   self.snakeDirection[i] = self.snakeCorner[ci][2]

                   if i == 0:
                       self.re_to_cha_Dir = True

                   if i == len(self.snakeX)-1:
                       del self.snakeCorner[0]
                       break

            if self.snakeDirection[i] == Snake.UP:
                self.snakeY[i] -= Snake.vel

            elif self.snakeDirection[i] == Snake.DOWN:
                self.snakeY[i] += Snake.vel

            elif self.snakeDirection[i] == Snake.LEFT:
                self.snakeX[i] -= Snake.vel

            elif self.snakeDirection[i] == Snake.RIGHT:
              self.snakeX[i] += Snake.vel

            # runs twice when multiple extra snake blocks are added
            elif self.lastWait < 4:
                self.lastWait += 1
                break

            elif self.lastWait == 4:
                self.snakeDirection[self.currentLength] = self.lastDirection
                self.currentLength += 1
                self.lastWait += 1

                self.waitTails -= 1

                if self.waitTails > 0:
                    self.lastWait = 0
                break


    def _calcNextCorner(self, pos, rounding):
        if rounding % 2 == 0:
            diff = pos % 20

            nextCornerPos = pos - diff

            return nextCornerPos

        else:
            modulodiff = pos % 20

            diff = 20 - modulodiff

            nextCornerPos = pos + diff

            return nextCornerPos


    def setDirection(self, keys):
        if keys[pygame.K_UP] & self.re_to_cha_Dir:
            if self.snakeDirection[0] != Snake.UP and self.snakeDirection[0] != Snake.DOWN:

                self.re_to_cha_Dir = False

                self.snakeCorner.append([self._calcNextCorner(self.snakeX[0], self.snakeDirection[0]), self.snakeY[0], Snake.UP])

        elif keys[pygame.K_DOWN] & self.re_to_cha_Dir:
            if self.snakeDirection[0] != Snake.UP and self.snakeDirection[0] != Snake.DOWN:
                self.re_to_cha_Dir = False

                self.snakeCorner.append([self._calcNextCorner(self.snakeX[0], self.snakeDirection[0]), self.snakeY[0], Snake.DOWN])

        elif keys[pygame.K_RIGHT] & self.re_to_cha_Dir:
            if self.snakeDirection[0] != Snake.RIGHT and self.snakeDirection[0] != Snake.LEFT:
                self.re_to_cha_Dir = False

                self.snakeCorner.append([self.snakeX[0], self._calcNextCorner(self.snakeY[0], self.snakeDirection[0]), Snake.RIGHT])

        elif keys[pygame.K_LEFT] & self.re_to_cha_Dir:
            if self.snakeDirection[0] != Snake.RIGHT and self.snakeDirection[0] != Snake.LEFT:
                self.re_to_cha_Dir = False

                self.snakeCorner.append([self.snakeX[0], self._calcNextCorner(self.snakeY[0], self.snakeDirection[0]), Snake.LEFT])
        elif keys[pygame.K_SPACE] and (not self.snakeAlive or self.victory):
            self.__init__(self.win)
        elif keys[pygame.K_w]:
            self.cheatCode[0] = "W"
        elif keys[pygame.K_i]:
            self.cheatCode[1] = "I"
        elif keys[pygame.K_n]:
            self.cheatCode[2] = "N"

            cheat = ""
            for ch in self.cheatCode:
                cheat += str(ch)

            if cheat == "WIN":
                self.victory = True
                self.appleEaten = 99999999



    def _checkDead(self):
        if self.snakeX[0] < 0 or self.snakeX[0] > 480-Snake.dim or self.snakeY[0] < 0 or self.snakeY[0] > 480-Snake.dim:
            self.snakeAlive = False
            return

        headx = self.snakeX[0]
        heady = self.snakeY[0]
        headDir = self.snakeDirection[0]

        for i in range(1, len(self.snakeX)):
             if (headx+Snake.dim > self.snakeX[i] and headx+Snake.dim < self.snakeX[i]+Snake.dim) and headDir == Snake.RIGHT and (heady > self.snakeY[i]-Snake.dim and heady < self.snakeY[i]+Snake.dim):
                 self.snakeAlive = False
                 return
             elif (headx < self.snakeX[i]+Snake.dim and headx > self.snakeX[i]) and headDir == Snake.LEFT and (heady > self.snakeY[i]-Snake.dim and heady < self.snakeY[i]+Snake.dim):
                 self.snakeAlive = False
                 return
             elif (heady+Snake.dim > self.snakeY[i] and heady+Snake.dim < self.snakeY[i]+Snake.dim) and headDir == Snake.DOWN and (headx > self.snakeX[i]-Snake.dim and headx < self.snakeX[i]+Snake.dim):
                 self.snakeAlive = False
                 return
             elif (heady < self.snakeY[i]+Snake.dim and heady > self.snakeY[i]) and headDir == Snake.UP and (headx > self.snakeX[i]-Snake.dim and headx < self.snakeX[i]+Snake.dim):
                 self.snakeAlive = False
                 return

    def snakeGrow(self):
        print("snake grows!")

        lastSnakeX = self.snakeX[-1]
        lastSnakeY = self.snakeY[-1]

        if self.waitTails == 0:
            self.lastWait = 0
            self.lastDirection = self.snakeDirection[-1]



        for i in range(self.growthRate):
            self.snakeX.append(lastSnakeX)
            self.snakeY.append(lastSnakeY)
            self.snakeDirection.append(None)

        self.waitTails += self.growthRate





    def render(self):

        if self.snakeMove & self.snakeAlive & (not self.victory):
            self._forward()
            self._checkDead()

        for i in range(len(self.snakeX)):
            if i == 0:
                pygame.draw.rect(self.win, (0, 100, 0), (self.snakeX[i], self.snakeY[i], Snake.dim, Snake.dim))
            else:
                pygame.draw.rect(self.win, (0, 255, 0), (self.snakeX[i], self.snakeY[i], Snake.dim, Snake.dim))

        cheat = ""
        for ch in self.cheatCode:
            cheat += str(ch)

        if cheat == "WIN":
            self.victory = True

    def __str__(self):
        return "ssssssssss"
