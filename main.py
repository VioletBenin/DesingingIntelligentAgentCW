import pygame
from grid import Grid
from win import draw, get_random_pos
from star_algorithm import multi_algorithm
from constant import *



def main(win):
    grids = [Grid(ROWS, WIDTH) for _ in range(3)]

    ifQuit = False

# quit windows
    while not ifQuit:     
        _grid = Grid(ROWS, WIDTH)       
        num_cars = 3
        starts_ends = []

        for i in range(num_cars):
            start = get_random_pos(_grid.grid)
            end = get_random_pos(_grid.grid)
            while end == start:
                end = get_random_pos(_grid.grid)
            starts_ends.append((start, end))

        for i, (start, end) in enumerate(starts_ends):
            start.make_start(COLORS[i])
            end.make_end(COLORS[i])

        run = True
        message = ""

        while run:
            draw(_grid, win, message)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    ifQuit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reset
                        run = False
                        break
                    if event.key == pygame.K_q:  # Quit
                        run = False
                        ifQuit = True
                    if event.key == pygame.K_SPACE:
                        for row in _grid.grid:
                            for spot in row:
                                spot.update_neighbors(_grid.grid)
                        all_paths_found = multi_algorithm(lambda: draw(_grid, win, message), _grid.grid, starts_ends)
                        if all_paths_found:
                            message = "All Paths Found"
                        else:
                            message = "No Path Found for Some Cars"

if __name__ == "__main__":
    
    WIN_WIDTH = WIDTH * 3  # Assuming WIDTH is the width of a single grid
    WIN_HEIGHT = WIDTH     # Assuming the height you want is equal to the grid width
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT+ 270))
    pygame.display.set_caption("Path Finding Algorithm Across Three Grids：Cooperative A*, Priority, Genetic")
    main(WIN)
    pygame.quit()