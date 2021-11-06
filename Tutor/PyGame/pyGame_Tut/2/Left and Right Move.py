import pygame
import sys

FPS = 60
W = 700  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

iteration = 0

running = True
motion = 'STOP'
sc.fill(WHITE)
pygame.draw.circle(sc, BLUE, (x, y), r)
pygame.display.update()
clock.tick(FPS)



while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = 'LEFT'
            elif i.key == pygame.K_RIGHT:
                motion = 'RIGHT'
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT,
                         pygame.K_RIGHT]:
                motion = 'STOP'

    if motion == 'LEFT':
        if x > 0 + r:
            x -= 3
    elif motion == 'RIGHT':
        if x < W-r:
            x += 3


    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()

    clock.tick(FPS)