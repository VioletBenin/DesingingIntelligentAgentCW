import pygame
import random


# window settings
# cell_size = 1
cell_size = 10
# grid_cells = 200
grid_cells = 50
margin = 10
width = grid_cells * cell_size * 3 + margin * 4
height = grid_cells * cell_size + margin * 2
screen = pygame.display.set_mode((width, height))
window_caption="Three Multi-Robots Path Planning Algorithm Demonstrations"


# color setting
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# 10-30
obstacles_rate=15
obstacles = {(random.randint(0, grid_cells - 1), random.randint(0, grid_cells - 1)) for _ in range(grid_cells*obstacles_rate)}


start_point = (0, 0)
goal_point = (grid_cells - 1, grid_cells - 1)


def draw_grid(x_offset, path=None, color=black):
    for x in range(grid_cells):
        for y in range(grid_cells):
            rect = pygame.Rect(x * cell_size + x_offset, y * cell_size + margin, cell_size, cell_size)
            pygame.draw.rect(screen, black, rect, 1) 
            if path and (x, y) in path:
                pygame.draw.rect(screen, color, rect)

def draw_obstacles(x_offset, obstacles, color=black):
    for x, y in obstacles:
        rect = pygame.Rect(x * cell_size + x_offset, y * cell_size + margin, cell_size, cell_size)
        pygame.draw.rect(screen, color, rect) 


robot_number=5

robots = []
for _ in range(robot_number):
    start = (random.randint(0, grid_cells - 1), random.randint(0, grid_cells - 1))
    goal = (random.randint(0, grid_cells - 1), random.randint(0, grid_cells - 1))
    robots.append({'start': start, 'goal': goal})
# robots[0]['goal'] = (new_goal_x, new_goal_y) 



# priority algorithm

def astar_path(start, goal, obstacles):
    from heapq import heappop, heappush
    from collections import deque

    def heuristic(a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return set(data)

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < grid_cells and 0 <= neighbor[1] < grid_cells and neighbor not in obstacles:
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heappush(oheap, (fscore[neighbor], neighbor))
                
    return set()

def priority_algorithm():
    path = set()    
    for robot in robots:
        path.update(astar_path(robot['start'], robot['goal'], obstacles))
    return path

# cooperative A*

def cooperative_astar(start, goal, obstacles, paths):
    obstacles = obstacles.union(paths)
    return astar_path(start, goal, obstacles)

def cooperative_a_star():
    path = set()
    for robot in robots:
        path.update(cooperative_astar(robot['start'], robot['goal'], obstacles, path))  
    return path




def initialize_population(start, goal, population_size=grid_cells, path_length=grid_cells):
    import random
    population = []
    for _ in range(population_size):
        path = [start]
        current_position = start
        for _ in range(path_length - 1):

            next_step = (current_position[0] + random.choice([-1, 0, 1]),
                         current_position[1] + random.choice([-1, 0, 1]))
            next_step = (max(0, min(grid_cells - 1, next_step[0])),
                         max(0, min(grid_cells - 1, next_step[1])))
            path.append(next_step)
            current_position = next_step
        population.append(path)  
    return population

def evolve_population(population, mutation_rate=0.01):
    new_population = []
    for _ in range(len(population)):
        parent1 = random.choice(population)
        parent2 = random.choice(population)


        cross_point = random.randint(0, len(parent1) - 1)
        child = parent1[:cross_point] + parent2[cross_point:]


        if random.random() < mutation_rate:
            mutate_point = random.randint(0, len(child) - 1)
            child[mutate_point] = (child[mutate_point][0] + random.choice([-1, 0, 1]),
                                   child[mutate_point][1] + random.choice([-1, 0, 1]))

        new_population.append(child)

    return new_population

def genetic_algorithm(start, goal):
    population = initialize_population(start, goal)
    for generation in range(100):
        population = evolve_population(population)
        for path in population:
            if path[-1] == goal and len(path) <= grid_cells*grid_cells: 
                return path
    return min(population, key=lambda p: len(p)) 



start_point = (0, 0)
goal_point = (grid_cells - 1, grid_cells - 1)

paths = {
    "priority": set(),
    "cooperative": set(),
    "genetic": set()
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
        
        draw_obstacles(margin, obstacles, black)
        draw_obstacles(grid_cells * cell_size + 2 * margin, obstacles, black)
        draw_obstacles(2 * (grid_cells * cell_size + margin) + margin, obstacles, black)


        if not paths["priority"]:
            paths["priority"] = priority_algorithm()
        if not paths["cooperative"]:
            paths["cooperative"] = cooperative_a_star()
        if not paths["genetic"]:
            paths["genetic"] = genetic_algorithm(start_point,goal_point)


        draw_grid(margin, paths["priority"], red)
        draw_grid(grid_cells * cell_size + 2 * margin, paths["cooperative"], green)
        draw_grid(2 * (grid_cells * cell_size + margin) + margin, paths["genetic"], blue)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()