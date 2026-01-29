def dfs(graph, start):
    """
    graph: adjacency list (dict) -> {node: [neighbors]}
    start: starting node
    """

    visited = set()

    def dfs_visit(node):
        visited.add(node)        # mark as visited immediately
        print(node, end=" ")     # process the node

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)
