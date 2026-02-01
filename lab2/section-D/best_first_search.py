import heapq

def best_first_search(graph, start, goal, heuristic):
    """
    graph: dict {node: [neighbors]}
    heuristic: dict {node: h(node)}
    """

    # Priority queue: (heuristic_value, node)
    pq = []
    heapq.heappush(pq, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while pq:
        h, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        # Goal test
        if current == goal:
            return reconstruct_path(parent, goal)

        # Expand neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return None  # Goal not found


def reconstruct_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]




graph = {
    'A': ['B','C','D'],
    'B': ['A','E'],
    'C': ['A','E','F'],
    'D': ['A','F'],
    'E': ['B','C','H'],
    'F': ['C','D','G'],
    'G': ['F','H'],
    'H': ['E','G']
}

heuristic = {
    'A': 39,
    'B': 31,
    'C': 24,
    'D': 34,
    'E': 18,
    'F': 16,   
    'G': 0,  # goal
    'H': 9
}

path = best_first_search(graph, 'A', 'G', heuristic)
print(path) # ['A', 'C', 'F', 'G']
