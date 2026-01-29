def dfs_iterative(graph, start):
    visited = set()
    stack = [start]    # DFS uses a stack (LIFO)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            # reverse to match recursive DFS order (optional)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
