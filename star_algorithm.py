import pygame
from queue import PriorityQueue
from constant import *
from node import Node

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = distance(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end(end.color)
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + distance(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def multi_algorithm(draw, grid, starts_ends):
    counts = [0] * len(starts_ends)
    open_sets = [PriorityQueue() for _ in starts_ends]
    came_from_list = [{} for _ in starts_ends]
    g_scores = [{spot: float("inf") for row in grid for spot in row} for _ in starts_ends]
    f_scores = [{spot: float("inf") for row in grid for spot in row} for _ in starts_ends]
    open_set_hashes = [set() for _ in starts_ends]

    for i, (start, end) in enumerate(starts_ends):
        open_sets[i].put((0, counts[i], start))
        g_scores[i][start] = 0
        f_scores[i][start] = distance(start.get_pos(), end.get_pos())
        open_set_hashes[i].add(start)

    all_found = [False] * len(starts_ends)
    while any(not found for found in all_found):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for i, (start, end) in enumerate(starts_ends):
            if all_found[i]:
                continue

            if not open_sets[i].empty():
                current = open_sets[i].get()[2]
                open_set_hashes[i].remove(current)

                if current == end:
                    reconstruct_path(came_from_list[i], end, draw)
                    end.make_end(end.color)
                    all_found[i] = True
                    continue

                for neighbor in current.neighbors:
                    temp_g_score = g_scores[i][current] + 1

                    if temp_g_score < g_scores[i][neighbor]:
                        came_from_list[i][neighbor] = current
                        g_scores[i][neighbor] = temp_g_score
                        f_scores[i][neighbor] = temp_g_score + distance(neighbor.get_pos(), end.get_pos())
                        if neighbor not in open_set_hashes[i]:
                            counts[i] += 1
                            open_sets[i].put((f_scores[i][neighbor], counts[i], neighbor))
                            open_set_hashes[i].add(neighbor)
                            neighbor.make_open()

                draw()

                if current != start:
                    current.make_closed()

    return all(all_found)