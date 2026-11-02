# B2 DFS Water Jug - state (x, y). Try 6 moves, go deep, backtrack on dead end.
a, b, target = map(int, input("Jug X, jug Y, target (e.g. 4 3 2): ").split())
visited, path = set(), []

def dfs(x, y):
    if (x, y) in visited:
        return False
    visited.add((x, y))
    path.append((x, y))
    if x == target or y == target:
        return True
    p, q = min(x, b - y), min(y, a - x)       # amount poured X->Y and Y->X
    for nx, ny in [(a, y), (x, b), (0, y), (x, 0), (x - p, y + p), (x + q, y - q)]:
        if dfs(nx, ny):
            return True
    path.pop()                                # backtrack
    return False

print(path if dfs(0, 0) else "No solution")
