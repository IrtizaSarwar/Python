import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS, BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (237, 7, 7)
TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(BG_COLOR)
font = pygame.font.Font(None, 60)
board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_lines():
    for i in range(1, BOARD_ROWS):

        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, I * SQUARE_SIZE), LINE_WIDTH)

        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE,0), (WIDTH, i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE = SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def check_winner(player):

    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            return True
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range)[BOARD_ROWS]:
            return True
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_ROWS - 1 - I] == player for i in range(BOARD_ROWS)):
        return True
    return False

def show_message(message):
    screen.fill(BG_COLOR)
    text = font.render(message, True, TEXT_COLOR)
    text_react = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_react)
    pygame.display.update()
    pygame.time.delay(3000)

def restart():
    global board
    board = [[" " for row in range(BOARD_COLS)] for _ in range(BOARD_COLS)]
    screen.fill(BG_COLOR)
    draw_lines()

def is_full():
    return all(cell != " " for row in board for cell in row)

draw_lines()
player = 'X'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if board[clicked_row][clicked_col] == " ":
                board[clicked_row][clicked_col] = player
                if check_winner(player):
                    show_message(f"Player {player} wins!")
                    restart()
                elif if_full():
                    show_message("It's a tie!")
                    restart()
                player = 'O' if player == 'X' else 'X'

        draw_figures()

    pygame.display.update