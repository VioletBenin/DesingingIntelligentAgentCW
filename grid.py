import pygame
import constant
import node

def draw_text(win, text):
    pygame.font.init() 
    font = pygame.font.SysFont('Arial', 20)
    text_surface = font.render(text, True, constant.BLACK)  # 创建文本图像
    win.blit(text_surface, (10, constant.WIDTH + 20))  # 绘制文本图像到窗口

class Grid:       
    def __init__(self, rows, width):
        self.rows=rows
        self.width=width
        self.grid = []
        self.gap = width // rows  
        
        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                spot = node.Node(i, j, self.gap, rows)
                self.grid[i].append(spot)
        # return self

    # draw map 
    def draw_grid(self,win): 
        # gap = width // rows
        for i in range(self.rows):
            pygame.draw.line(win, constant.GREY, (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                pygame.draw.line(win, constant.GREY, (j * self.gap, 0), (j * self.gap, self.width))

    def draw(self,win):
        win.fill(constant.WHITE)
        for row in self.grid:
            for spot in row:
                spot.draw(win)
        self.draw_grid(win)
        draw_text(win, "Left：设置起点/终点/障碍物，右键：取消，空格：开始寻路，R：重置")  
        pygame.display.update()

    def get_clicked_pos(self,pos, rows, width):
        # gap = width // rows
        y, x = pos
        row = y // self.gap
        col = x // self.gap
        return row, col


# ??
    def reset_grid(self,grid, rows):
        for row in range(rows):
            for col in range(rows):
                grid[row][col].reset()  
        return grid

