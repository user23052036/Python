def depth_limited_search(graph, start, goal, limit):
    """
    graph : adjacency list {node: [neighbors]}
    start : start node
    goal  : goal node
    limit : maximum depth allowed
    """

    def dls(node, depth):
        # Goal test
        if node == goal:
            return True

        # Depth limit reached
        if depth == limit:
            return False

        # Explore neighbors
        for neighbor in graph[node]:
            if dls(neighbor, depth + 1):
                return True

        return False

    return dls(start, 0)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(depth_limited_search(graph, 'A', 'F', limit=2))  # True
print(depth_limited_search(graph, 'A', 'F', limit=1))  # False
