import constant
import pygame

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.constant = constant.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.constant == constant.RED

    def is_open(self):
        return self.constant == constant.GREEN

    def is_barrier(self):
        return self.constant == constant.BLACK

    def is_start(self):
        return self.constant == constant.ORANGE

    def is_end(self):
        return self.constant == constant.TURQUOISE

    def reset(self):
        self.constant = constant.WHITE

    def make_start(self):
        self.constant = constant.ORANGE

    def make_closed(self):
        self.constant = constant.RED

    def make_open(self):
        self.constant = constant.GREEN

    def make_barrier(self):
        self.constant = constant.BLACK

    def make_end(self):
        self.constant = constant.TURQUOISE

    def make_path(self):
        self.constant = constant.PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.constant, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # 不是障碍
            self.neighbors.append(grid[self.row - 1][self.col])  # 添加上方节点为邻居

        # 仅在节点不在最后一行时检查下方节点
        if self.row < len(grid) - 1 and not grid[self.row + 1][self.col].is_barrier():  # 不是障碍
            self.neighbors.append(grid[self.row + 1][self.col])  # 添加下方节点为邻居

        # 仅在节点不在第一列时检查左侧节点
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # 不是障碍
            self.neighbors.append(grid[self.row][self.col - 1])  # 添加左侧节点为邻居

        # 仅在节点不在最后一列时检查右侧节点
        if self.col < len(grid[0]) - 1 and not grid[self.row][self.col + 1].is_barrier():  # 不是障碍
            self.neighbors.append(grid[self.row][self.col + 1])  # 添加右侧节点为邻居

    def reset(self):
        self.is_barrier = False
        self.is_start = False
        self.is_end = False
        self.is_path = False
        self.constant = constant.WHITE