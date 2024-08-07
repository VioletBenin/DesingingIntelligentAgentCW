import pygame

def draw_grid(screen, grid_cells, cell_size, x_offset, path=None, start=None, goal=None, path_color=(0, 0, 0), start_color=(128, 128, 128), goal_color=(128, 128, 128)):
    for x in range(grid_cells):
        for y in range(grid_cells):
            rect = pygame.Rect(x * cell_size + x_offset, y * cell_size + 10, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
            if path and (x, y) in path:
                pygame.draw.rect(screen, path_color, rect)
            if start == (x, y):
                pygame.draw.rect(screen, start_color, rect)
            if goal == (x, y):
                pygame.draw.rect(screen, goal_color, rect)

def draw_obstacles(screen, grid_cells, cell_size, x_offset, obstacles, color=(0, 0, 0), start=None, goal=None, start_color=(128, 128, 128), goal_color=(128, 128, 128)):
    for x, y in obstacles:
        rect = pygame.Rect(x * cell_size + x_offset, y * cell_size + 10, cell_size, cell_size)
        pygame.draw.rect(screen, color, rect)
    if start:
        rect = pygame.Rect(start[0] * cell_size + x_offset, start[1] * cell_size + 10, cell_size, cell_size)
        pygame.draw.rect(screen, start_color, rect)
    if goal:
        rect = pygame.Rect(goal[0] * cell_size + x_offset, goal[1] * cell_size + 10, cell_size, cell_size)
        pygame.draw.rect(screen, goal_color, rect)
