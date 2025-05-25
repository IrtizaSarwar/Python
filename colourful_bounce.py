import pygame
import random
pygame.init()

CHANGE_COLOUR_SPRITE = pygame.USEREVENT + 1
CHANGE_COLOUR_BG = pygame.USEREVENT + 2

VIOLET = pygame.color('violet')
BLUE = pygame.color('blue')
SKY_BLUE = pygame.color('sky_blue')
GREEN = pygame.color('green')

YELLOW = pygame.color('yellow')
ORANGE = pygame.color('orange')
RED = pygame.color('red')
WHITE = pygame.color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width):
        super.__init__()
        self.image = pygame.Surface([widht, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1, 1])]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >=400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(CHANGE_COLOUR_SPRITE))
            pygame.event.post(pygame.event.Event(CHANGE_COLOUR_BG))

    def change_color(self):
        self.image.fill = (random.choice([VIOLET, GREEN, RED, BLUE]))
    

def change_bg_color(self):
    global bg_color
    bg_color = random.choice([SKY_BLUE, YELLOW, ORANGE, WHITE])

all_sprites = pygame.sprite.Group()
sp1 = (WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0,370)
all_sprites.add(sp1)

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Colourful Bounce")
bg_color = BLUE
screen_fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit == True
        elif event.type == CHANGE_COLOUR_SPRITE:
            sp1.change_colour()
        elif event.type == CHANGE_COLOUR_BG:
            change_bg_color()
    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()