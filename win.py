
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
            
            

# messages = {
#     "default":"R-click to cancel; R key to start again; Q key to exit."
#     "start": "L-click to set starting point.",
#     "end": "L-click to set the end point.",
#     "obstacle": "L-click to set obstacles;Space to navigate."
# }



# # 初始状态
# current_stage = "start"

            
            
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:  # 左键
#                     if current_stage == "start":
#                         # 设置起点逻辑
#                         current_stage = "end"
#                     elif current_stage == "end":
#                         # 设置终点逻辑
#                         current_stage = "obstacle"
#                     elif current_stage == "obstacle":
#                         # 设置障碍物逻辑
#                 elif event.button == 3:  # 右键
#                     # 取消逻辑
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_r:
#                     # 重置逻辑
#                     current_stage = "start"

#     # 在每次循环中调用 draw 函数
#             draw(WIN, grid, ROWS, WIDTH, font, messages[current_stage])

            
            
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
                if event.key == pygame.K_r:  # 按 R 键重置
                    start = None
                    end = None
                    _grid = _grid.reset__grid(_grid, constant.ROWS)
                    started = False


                elif event.key == pygame.K_SPACE and start and end:
                    for row in _grid.grid:
                        for spot in row:
                            spot.update_neighbors(_grid.grid)
                    star_algorithm.algorithm(lambda: draw(_grid,win), _grid.grid, start, end)
