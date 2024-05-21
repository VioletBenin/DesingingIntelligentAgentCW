import pygame
import constant
import node, random

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

        
        # obstacle_probability=0.2
        # # grid = []
        # for i in range(rows):
        #     row = []
        #     for j in range(rows):
        #         cell = 0 if random.random() > obstacle_probability else 1  # 0 ，1 ob
        #         row.append(cell)
        #     self.grid.append(row)
        # # return grid

    # draw map 
    def draw_grid(self,win): 
        for i in range(self.rows):
            pygame.draw.line(win, constant.GREY, (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                pygame.draw.line(win, constant.GREY, (j * self.gap, 0), (j * self.gap, self.width))

    def get_clicked_pos(self,pos, rows, width):
        y, x = pos
        row = y // self.gap
        col = x // self.gap
        return row, col