import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
BLUE = (0, 100, 255)

player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 100, 50, 90)
enemy_width, enemy_height = 50, 90
enemies = []
enemy_speed = 5
spawn_timer = 0
spawn_delay = 1000

score = 0
font = pygame.font.SysFont("Roboto", 28)
game_over = False

def reset():
    global enemies, score, game_over, spawn_timer
    player.x = WIDTH // 2 - 25
    enemies.clear()
    score = 0
    game_over = False
    spawn_timer = pygame.time.get_ticks()

def spawn_enemy():
    x = random.randint(20, WIDTH - enemy_width - 20)
    enemy = pygame.Rect(x, -enemy_height, enemy_width, enemy_height)
    enemies.append(enemy)

def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed

def check_collision():
    for enemy in enemies:
        if player.colliderect(enemy):
            return True
    return False

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

reset()
running = True

while running:
    clock.tick(60)
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset()

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= 5
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += 5

        move_enemies()

        now = pygame.time.get_ticks()
        if now - spawn_timer > spawn_delay:
            spawn_enemy()
            spawn_timer = now

        enemies = [e for e in enemies if e.top < HEIGHT]

        for enemy in enemies:
            if enemy.bottom == HEIGHT:
                score += 1

        if check_collision():
            game_over = True

    pygame.draw.rect(screen, BLUE, player)
    draw_enemies()
    draw_score()

    if game_over:
        msg = font.render("PRESS R TO RESTART!", True, WHITE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()
