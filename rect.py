import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (0,0,255), (400,300,100,70))

    pygame.display.flip()