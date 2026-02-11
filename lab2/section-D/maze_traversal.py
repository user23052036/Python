from collections import deque

maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1]
]

start = (0, 0)
end = (4, 4)

def bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored = 0

    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored, len(visited)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] == 1 and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored, len(visited)


def dfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    stack = [(start, [start])]
    visited = set([start])
    nodes_explored = 0

    while stack:
        (x, y), path = stack.pop()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored, len(visited)

        for dx, dy in reversed(directions):
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] == 1 and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored, len(visited)


# Run both
bfs_path, bfs_explored, bfs_visited = bfs(maze, start, end)
dfs_path, dfs_explored, dfs_visited = dfs(maze, start, end)

print("===== RESULTS =====")
print("BFS Path (Shortest):", bfs_path)
print("DFS Path (Any valid):", dfs_path)

print("\n===== NODE COMPARISON =====")
print(f"BFS Nodes Expanded : {bfs_explored}")
print(f"DFS Nodes Expanded : {dfs_explored}")

print(f"BFS Total Visited  : {bfs_visited}")
print(f"DFS Total Visited  : {dfs_visited}")

print("\nDifference in Expanded Nodes:",
      abs(bfs_explored - dfs_explored))
