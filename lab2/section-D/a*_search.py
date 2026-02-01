import heapq

def a_star(graph, start, goal, heuristic):
    # priority queue: (f = g + h, node)
    pq = []
    heapq.heappush(pq, (heuristic[start], start))

    g_cost = {start: 0}
    parent = {start: None}

    while pq:
        f, current = heapq.heappop(pq)

        if current == goal:
            return reconstruct_path(parent, goal)

        for neighbor, weight in graph[current]:
            new_g = g_cost[current] + weight

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, neighbor))

    return None


def reconstruct_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]


graph = {
    'A': [('B', 8), ('C', 5), ('D', 9)],
    'B': [('A', 8), ('E', 7)],
    'C': [('A', 5), ('E', 6), ('F', 4)],
    'D': [('A', 9), ('F', 8)],
    'E': [('B', 7), ('C', 6), ('H', 5)],
    'F': [('C', 4), ('D', 8), ('G', 6)],
    'G': [('F', 6), ('H', 3)],
    'H': [('E', 5), ('G', 3)]
}
heuristic = {
    'A': 39,
    'B': 31,
    'C': 24,
    'D': 34,
    'E': 18,
    'F': 16,   
    'G': 0,   # goal
    'H': 9
}

path = a_star(graph, 'A', 'G', heuristic)
print(path)
