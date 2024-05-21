import pygame,random
from constant import *

def draw_text(win, text, pos):
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 20)
    text_surface = font.render(text, True, BLACK)
    win.blit(text_surface, (10, pos))

def draw(grid, win, message):
    win.fill(WHITE)
    for row in grid.grid:
        for spot in row:
            spot.draw(win)
    grid.draw_grid(win)
    draw_text(win, "Press [R] to reset.", WIDTH + 20)
    draw_text(win, "Press [Q] to quit.", WIDTH + 70)
    draw_text(win, "Press [Space] to find route.", WIDTH + 120)
    draw_text(win, message, WIDTH + 170)
    pygame.display.update()

def get_random_pos(grid):
    while True:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, ROWS - 1)
        if not grid[row][col].is_barrier():
            return grid[row][col]
