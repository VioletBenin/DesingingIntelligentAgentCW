import pygame
import random
from node import Node
from constant import *

class Grid:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.grid = []
        self.gap = width // rows

        for i in range(rows):
            self.grid.append([])
            for j in range(rows):
                spot = Node(i, j, self.gap, rows)
                if random.random() < 0.15:  # 15% chance to generate barriers
                    spot.make_barrier()
                self.grid[i].append(spot)

    def draw_grid(self, win):
        for i in range(self.rows):
            pygame.draw.line(win, GREY, (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                pygame.draw.line(win, GREY, (j * self.gap, 0), (j * self.gap, self.width))

    def get_clicked_pos(self, pos):
        y, x = pos
        row = y // self.gap
        col = x // self.gap
        return row, col
