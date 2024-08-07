from heapq import heappop, heappush

def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def astar_path(start, goal, obstacles, grid_cells):
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
            data.append(start)
            data.reverse()
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < grid_cells and 0 <= neighbor[1] < grid_cells and neighbor not in obstacles:
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heappush(oheap, (fscore[neighbor], neighbor))
                
    return []

def path_cost(path):
    return len(path) - 1  # since we are using a grid and each step costs 1

def yen_k_shortest_paths(start, goal, obstacles, grid_cells, K):
    A = [astar_path(start, goal, obstacles, grid_cells)]
    B = []

    for k in range(1, K):
        for i in range(len(A[k-1]) - 1):
            spur_node = A[k-1][i]
            root_path = A[k-1][:i+1]
            
            removed_edges = []
            for path in A:
                if path[:i+1] == root_path and len(path) > i+1:
                    removed_edge = (path[i], path[i+1])
                    if removed_edge[1] not in obstacles:
                        obstacles.add(removed_edge[1])  # temporarily remove this edge
                        removed_edges.append(removed_edge[1])
                    
            spur_path = astar_path(spur_node, goal, obstacles, grid_cells)
            
            if spur_path:
                total_path = root_path[:-1] + spur_path
                if total_path not in B:
                    heappush(B, (path_cost(total_path), total_path))
            
            for edge in removed_edges:
                obstacles.remove(edge)  # restore the removed edges
        
        if not B:
            break
        
        cost, path = heappop(B)
        A.append(path)
    
    # return A
    return A

def priority_algorithm(robots, obstacles, grid_cells, K=3):
    paths = set()    
    for robot in robots:
        robot_paths = yen_k_shortest_paths(robot['start'], robot['goal'], obstacles, grid_cells, K)
        for path in robot_paths:
            paths.update(path)
    return paths

def cooperative_astar(start, goal, obstacles, paths, grid_cells):
    obstacles = obstacles.union(paths)
    return astar_path(start, goal, obstacles, grid_cells)

def cooperative_a_star(robots, obstacles, grid_cells, K=3):
    path = set()
    for robot in robots:
        path.update(cooperative_astar(robot['start'], robot['goal'], obstacles, path, grid_cells))
    return path
