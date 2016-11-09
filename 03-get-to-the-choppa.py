# https://www.codewars.com/kata/get-to-the-choppa/python


import heapq
from collections import deque


def heuristic(node, end_node):
    return abs(node.position.x - end_node.position.x) + abs(node.position.y - end_node.position.y)


def find_shortest_path(grid, start_node, end_node):
    if not grid:
        return grid

    parents = {start_node: None}
    cost_so_far = {start_node: 0}
    cost_to_the_end = {start_node: heuristic(start_node, end_node)}
    total_cost = {start_node: cost_so_far.get(start_node) + cost_to_the_end.get(start_node)}

    closed_nodes = deque()
    opened_nodes = []

    heapq.heapify(opened_nodes)
    heapq.heappush(opened_nodes, (total_cost.get(start_node), start_node))

    grid_height = len(grid)
    grid_width = len(grid[0])

    def find_neighbors(node):
        node = (node.position.x, node.position.y)
        result = []
        if node[0] > 0:
            result.append(grid[node[0] - 1][node[1]])
        if node[0] < grid_height - 1:
            result.append(grid[node[0] + 1][node[1]])
        if node[1] > 0:
            result.append(grid[node[0]][node[1] - 1])
        if node[1] < grid_width - 1:
            result.append(grid[node[0]][node[1] + 1])
        return result

    def update_node(child, parent):
        parents.update({child: parent})
        cost_so_far.update({child: cost_so_far.get(parent) + 1})
        cost_to_the_end.update({child: heuristic(child, end_node)})
        total_cost.update({child: cost_so_far.get(child) + cost_to_the_end.get(child)})

    def generate_path(node):
        path = []
        while parents.get(node):
            path.append(node)
            node = parents.get(node)
        return [start_node] + list(reversed(path))

    while opened_nodes:
        t_c, node = heapq.heappop(opened_nodes)
        closed_nodes.append(node)

        if node == end_node:
            return generate_path(node)

        neighbors = find_neighbors(node)
        for neighbor in neighbors:
            if neighbor not in closed_nodes and neighbor.passable:
                if (total_cost.get(neighbor), neighbor) in opened_nodes:
                    if total_cost.get(neighbor) > total_cost.get(node) + 1:
                        update_node(neighbor, node)
                else:
                    update_node(neighbor, node)
                    heapq.heappush(opened_nodes, (total_cost.get(neighbor), neighbor))
