
import pygame,constant,grid,star_algorithm

def draw_text(win, text, pos):
    pygame.font.init() 
    font = pygame.font.SysFont('Arial', 20)
    text_surface = font.render(text, True, constant.BLACK)  
    win.blit(text_surface, (10, pos))

def draw(grid0,win):
    win.fill(constant.WHITE)
    for row in grid0.grid:
        for spot in row:
            spot.draw(win)
    grid0.draw_grid(win) 
    # pos=constant.WIDTH + 20
    draw_text(win, "Press [R] to reset.",constant.WIDTH + 20)  
    draw_text(win, "Press [Q] to quit.",constant.WIDTH + 70) 
    draw_text(win, "L-click to select start, end and the barrier.",constant.WIDTH + 120) 
    draw_text(win, "R-click to remove the point.",constant.WIDTH + 170) 
    draw_text(win, "Press [Space] to find route.",constant.WIDTH + 220) 
    # Press [Space] to find route 
    pygame.display.update()

def main(win):
    ifQuit=False
    
    while(not ifQuit):
        _grid = grid.Grid(constant.ROWS, constant.WIDTH)
        start = None
        end = None
        run = True
        started = False
    
        while run:
            draw(_grid,win)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    ifQuit=True
                if started:
                    continue        
                
                # L-click to select start, end and the barrier
                if pygame.mouse.get_pressed()[0]:  
                    pos = pygame.mouse.get_pos()
                    row, col = _grid.get_clicked_pos(pos, constant.ROWS, constant.WIDTH)
                    spot = _grid.grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.make_start()
                    elif not end and spot != start:
                        end = spot
                        end.make_end()
                    elif spot != end and spot != start:
                        spot.make_barrier()

                 # R-click to remove those point
                elif pygame.mouse.get_pressed()[2]: 
                    pos = pygame.mouse.get_pos()
                    row, col = _grid.get_clicked_pos(pos, constant.ROWS, constant.WIDTH)
                    spot = _grid.grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    # Press [r] to reset 
                    if event.key == pygame.K_r:  
                        run = False
                        break
                    # Press [Q] to quit                    
                    if event.key == pygame.K_q:
                        run = False
                        ifQuit=True
                    # Press [Space] to find route
                    elif event.key == pygame.K_SPACE and start and end:
                        for row in _grid.grid:
                            for spot in row:
                                spot.update_neighbors(_grid.grid)
                        star_algorithm.algorithm(lambda: draw(_grid,win), _grid.grid, start, end)