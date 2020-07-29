import pygame
import snake
import apple

pygame.init()
pygame.font.init()

canvasLength = 480
canvasHeight = 480

win = pygame.display.set_mode((canvasLength, canvasHeight))

pygame.display.set_caption("Slange")


x = 50
y = 50
width = 20
height = 20


snake = snake.Snake(win)
apple = apple.Apple(win, snake)
apple1 = apple.Apple(win, snake)

# problem if more apples get eaten under growth


def drawGrid():
    for k in range(2):
        for i in range(0, canvasLength, 20):
            if k == 0:
                pygame.draw.line(win, (50, 50, 50), (i, 0), (i, canvasLength), 1)
            else:
                pygame.draw.line(win, (50, 50, 50), (0, i), (canvasHeight, i), 1)

def drawGameOver():
    myfont = pygame.font.SysFont('Sans', 75)
    myfont2 = pygame.font.SysFont('Sans', 30)

    win.blit(myfont.render('Game Over!', False, (255, 255, 255)), (100, 100))
    win.blit(myfont2.render('Press \'SPACE\' to try again', False, (255, 255, 255)), (120, 170))
    win.blit(myfont2.render('Apples eaten: ' + str(snake.appleEaten), False, (255, 255, 255)), (150, 200))


def drawGameWin():
    myfont = pygame.font.SysFont('Sans', 50)

    win.blit(myfont.render('You have a big snake!', False, (255, 255, 255)), (65, 100))
    win.blit(myfont.render('Thanks for playing!', False, (255, 255, 255)), (65, 150))

    myfont2 = pygame.font.SysFont('Sans', 30)
    win.blit(myfont2.render('Apples eaten: ' + str(snake.appleEaten), False, (255, 255, 255)), (150, 200))


run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.setDirection(pygame.key.get_pressed())

    win.fill((0, 0, 0))

    drawGrid()

    apple.render()
    apple1.render()
    snake.render()

    if not snake.snakeAlive:
        drawGameOver()

    if snake.victory:
        drawGameWin()

    pygame.display.update()

