
import pygame,constant,grid,star_algorithm



# "Left：设置起点/终点/障碍物，右键：取消，空格：开始寻路，R：重置"
def draw_text(win, text):
    pygame.font.init() 
    font = pygame.font.SysFont('Arial', 20)
    text_surface = font.render(text, True, constant.BLACK)  # 创建文本图像
    win.blit(text_surface, (10, constant.WIDTH + 20))  # 绘制文本图像到窗口

# def draw(grid0,win,text):
def draw(grid0,win):
    win.fill(constant.WHITE)
    for row in grid0.grid:
        for spot in row:
            spot.draw(win)
    grid0.draw_grid(win)
    # draw_text(win, text)  
    draw_text(win, "123")  
    pygame.display.update()

def main(win):
    
    
    while(1):
        _grid = grid.Grid(constant.ROWS, constant.WIDTH)
        start = None
        end = None
        run = True
        started = False
    
        while run:
            # _grid = grid.Grid(constant.ROWS, constant.WIDTH)
            # draw(win, _grid, constant.ROWS, constant.WIDTH)
            draw(_grid,win)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if started:
                    continue        
                
                # LEFT click to select start, end and the barrier
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

                 # RIGHT click to remove those point
                elif pygame.mouse.get_pressed()[2]: 
                    pos = pygame.mouse.get_pos()
                    row, col = _grid.get_clicked_pos(pos, constant.ROWS, constant.WIDTH)
                    spot = _grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  
                        print("reset")
                        
                        run = False
                        break
                        # start = None
                        # end = None
                        # # _grid = _grid.reset_grid(_grid, constant.ROWS)
                        # started = False

                    elif event.key == pygame.K_SPACE and start and end:
                        for row in _grid.grid:
                            for spot in row:
                                spot.update_neighbors(_grid.grid)
                        star_algorithm.algorithm(lambda: draw(_grid,win), _grid.grid, start, end)