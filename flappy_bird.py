import pygame
import random

pygame.init()
w, h = 400, 600
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

bird_y = h//2
bird_v = 0
g = 0.5
jump = -10
r = 15
x = 50

pipes = []
pipe_w = 60
gap = 150
speed = 3
score = 0
add_pipe = pygame.USEREVENT + 1
pygame.time.set_timer(add_pipe, 1500)

run = True
while run:
    win.fill((135, 206, 250))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bird_v = jump
        if e.type == add_pipe:
            t = random.randint(50, h - gap - 50)
            b = t + gap
            pipes.append({'x': w, 'top': t, 'bottom': b})

    bird_v += g
    bird_y += bird_v

    for p in pipes:
        p['x'] -= speed
        pygame.draw.rect(win, (0, 200, 0), (p['x'], 0, pipe_w, p['top']))
        pygame.draw.rect(win, (0, 200, 0), (p['x'], p['bottom'], pipe_w, h - p['bottom']))
        if p['x'] + pipe_w == x:
            score += 1

    pygame.draw.circle(win, (255, 255, 0), (x, int(bird_y)), r)
    win.blit(font.render(str(score), True, (0, 0, 0)), (10, 10))

    for p in pipes:
        if x + r > p['x'] and x - r < p['x'] + pipe_w:
            if bird_y - r < p['top'] or bird_y + r > p['bottom']:
                run = False
    if bird_y < 0 or bird_y > h:
        run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
