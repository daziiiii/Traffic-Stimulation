import pygame
import time

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Traffic Signal")

RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
DARK = (80,80,80)
WHITE = (255,255,255)

running = True
signal = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (150,100,100,350))

    r = RED if signal==0 else DARK
    y = YELLOW if signal==1 else DARK
    g = GREEN if signal==2 else DARK

    pygame.draw.circle(screen, r, (200,170), 40)
    pygame.draw.circle(screen, y, (200,270), 40)
    pygame.draw.circle(screen, g, (200,370), 40)

    pygame.display.update()

    time.sleep(2)
    signal = (signal + 1) % 3

pygame.quit()