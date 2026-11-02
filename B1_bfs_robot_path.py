# B1 BFS Robot Path - queue explores level by level, so first reach = shortest path.
from collections import deque

grid = [".....",
        ".###.",
        ".....",
        ".##..",
        "....."]
start, goal = (0, 0), (4, 4)
parent, q = {start: None}, deque([start])     # parent also acts as visited

while q:
    r, c = q.popleft()
    if (r, c) == goal:
        break
    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= nr < 5 and 0 <= nc < 5 and grid[nr][nc] == "." and (nr, nc) not in parent:
            parent[(nr, nc)] = (r, c)
            q.append((nr, nc))

if goal not in parent:
    print("No path")
else:
    path, p = [], goal
    while p:
        path.append(p)
        p = parent[p]
    print("Path:", path[::-1])
    print("Steps:", len(path) - 1)
