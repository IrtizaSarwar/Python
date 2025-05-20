import pygame
pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Solid Ball")
screen.fill((255,255,255))

green = (0, 255, 0)
red = (255, 0, 0)

pygame.draw.circle(screen, green, (300, 300), 50)
pygame.draw.circle(screen, red, (100, 100), 50, 5)

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()