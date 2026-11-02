# A2 Model-Based Agent - internal state = visited cells + path (stack).
# Move to a free unvisited neighbour; if none, go back (pop the path).
grid = ["...#.",
        "##.#.",
        ".....",
        ".###.",
        "...#."]
pos, goal = (0, 0), (4, 4)
visited, path = {pos}, [pos]

while pos != goal:
    r, c = pos
    for nr, nc in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:
        if 0 <= nr < 5 and 0 <= nc < 5 and grid[nr][nc] == "." and (nr, nc) not in visited:
            pos = (nr, nc)
            visited.add(pos)
            path.append(pos)
            break
    else:                       # no move possible -> backtrack using memory
        path.pop()
        if not path:
            print("Goal not reachable")
            break
        pos = path[-1]
    print("At", pos)
