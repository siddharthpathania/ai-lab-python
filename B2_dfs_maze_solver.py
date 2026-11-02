# B2 DFS Maze Solver - go deep in one direction; at a dead end, backtrack and try another way.
maze = ["..#..",
        ".##.#",
        "....#",
        "#.##.",
        "....."]
goal = (4, 4)
visited, path = set(), []

def dfs(r, c):
    if not (0 <= r < 5 and 0 <= c < 5) or maze[r][c] == "#" or (r, c) in visited:
        return False                      # outside, wall, or already visited
    visited.add((r, c))
    path.append((r, c))
    if (r, c) == goal:
        return True
    for nr, nc in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:   # right, down, left, up
        if dfs(nr, nc):
            return True
    path.pop()                            # dead end -> backtrack
    return False

if dfs(0, 0):
    print("Path:", path)
    print("Steps:", len(path) - 1)
    for r in range(5):                    # draw the maze, path shown as *
        row = ""
        for c in range(5):
            if (r, c) in path:
                row += "* "
            else:
                row += maze[r][c] + " "
        print(row)
else:
    print("No path")
