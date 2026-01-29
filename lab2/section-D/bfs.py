from collections import deque

def bfs(graph, start):
    """
    graph: adjacency list (dict) -> {node: [neighbors]}
    start: starting node
    """

    visited = set()          # keeps track of visited nodes
    queue = deque([start])   # BFS uses a queue (FIFO)

    visited.add(start)

    while queue:
        node = queue.popleft()   # take the front element
        print(node, end=" ")     # process the node (can be replaced)

        # explore all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)   # mark before enqueuing
                queue.append(neighbor)

# graph = {
#     0: [1, 2],
#     1: [0, 3, 4],
#     2: [0],
#     3: [1],
#     4: [1]
# }

# bfs(graph, 0)

# output: 0 1 2 3 4
