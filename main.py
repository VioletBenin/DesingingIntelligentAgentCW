import constant
import pygame
import win

if __name__ == "__main__":
    WIN = pygame.display.set_mode((constant.WIDTH, constant.WIDTH+270))
    pygame.display.set_caption("A* Path Finding Algorithm")
    win.main(WIN)
    pygame.quit()