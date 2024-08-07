import pygame
import random
from path_planning import priority_algorithm, cooperative_a_star,yen_k_algorithm 
from visualization import draw_grid, draw_obstacles

grid_cells = 20
# obstacles_rate = 0 
obstacles_rate = 20
# obstacles_rate = 30 
robots_number = 2

# window settings
cell_size = 10
margin = 10
width = grid_cells * cell_size * 3 + margin * 4
# grid+margin+text
height = grid_cells * cell_size + margin * 3 + 50  

window_caption = "Three Multi-Robots Path Planning Algorithm Visual Demonstrations"




screen = pygame.display.set_mode((width, height))


# color setting
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (128, 128, 128)

# Generate obstacles and robots
obstacles = {(random.randint(0, grid_cells - 1), random.randint(0, grid_cells - 1)) for _ in range(round(grid_cells* grid_cells * obstacles_rate * 0.01))}

robots = [{'start': (random.randint(0, grid_cells - 1), random.randint(0, grid_cells - 1)),
           'goal': (random.randint(0, grid_cells - 1), random.randint(0, grid_cells - 1))} for _ in range(robots_number)]



paths = {
    "priority": set(),
    "cooperative": set(),
    "yen_k": set()
}

def main():
    pygame.init()
    pygame.display.set_caption(window_caption)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)


        if not paths["priority"]:
            paths["priority"] = priority_algorithm(robots, obstacles, grid_cells, K=1)
        if not paths["cooperative"]:
            paths["cooperative"] = cooperative_a_star(robots, obstacles, grid_cells, K=1)
        if not paths["yen_k"]:
            paths["yen_k"] = yen_k_algorithm(robots, obstacles, grid_cells, K=1)

        print(robots)
        print(paths)
        
        
        # 目标点为什么默认在路径里
        success_priority = sum(1 for robot in robots if (robot['goal'] in paths["priority"]))
        success_cooperative = sum(1 for robot in robots if (robot['goal'] in paths["cooperative"]))
        success_yen_k = sum(1 for robot in robots if (robot['goal'] in paths["yen_k"]))

        print(success_priority)


        draw_obstacles(screen, grid_cells, cell_size, margin, obstacles, black)
        draw_obstacles(screen, grid_cells, cell_size, grid_cells * cell_size + 2 * margin, obstacles, black)
        draw_obstacles(screen, grid_cells, cell_size, 2 * (grid_cells * cell_size + margin) + margin, obstacles, black)


        font = pygame.font.SysFont(None, 36)
        text_priority = font.render(f'Priority: {success_priority}/{robots_number}', True, black)
        text_cooperative = font.render(f'Cooperative: {success_cooperative}/{robots_number}', True, black)
        text_yen_k = font.render(f'Yen\'s K: {success_yen_k}/{robots_number}', True, black)



# 只有一个有?i干么的
        # for robot in enumerate(robots):
        for i, robot in enumerate(robots):
            draw_grid(screen, grid_cells, cell_size, margin, paths["priority"], start=robot['start'], goal=robot['goal'], path_color=red, start_color=grey, goal_color=grey)
            draw_grid(screen, grid_cells, cell_size, grid_cells * cell_size + 2 * margin, paths["cooperative"], start=robot['start'], goal=robot['goal'], path_color=green, start_color=grey, goal_color=grey)
            draw_grid(screen, grid_cells, cell_size, 2 * (grid_cells * cell_size + margin) + margin, paths["yen_k"], start=robot['start'], goal=robot['goal'], path_color=blue, start_color=grey, goal_color=grey)



        screen.blit(text_priority, (margin, grid_cells * cell_size + 2 * margin + 10))
        screen.blit(text_cooperative, (width // 3 + margin, grid_cells * cell_size + 2 * margin + 10))
        screen.blit(text_yen_k, (2 * width // 3 + margin, grid_cells * cell_size + 2 * margin + 10))

        pygame.display.flip()

    pygame.quit()
    
    


if __name__ == "__main__":
    main()
    
