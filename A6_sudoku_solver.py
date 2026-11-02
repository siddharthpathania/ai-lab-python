# A6 Sudoku - backtracking + constraint propagation.
# Find options of every empty cell: 0 options -> dead end; fill cell with FEWEST options first (MRV).
rows = ["530070000", "600195000", "098000060", "800060003", "400803001",
        "700020006", "060000280", "000419005", "000080079"]
g = [[int(ch) for ch in row] for row in rows]

def ok(r, c, v):                  # not in row, column or 3x3 box
    br, bc = r // 3 * 3, c // 3 * 3
    return all(g[r][i] != v and g[i][c] != v and g[br + i // 3][bc + i % 3] != v for i in range(9))

def solve():
    best = None
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                opts = [v for v in range(1, 10) if ok(r, c, v)]
                if not opts:
                    return False                      # dead end
                if best is None or len(opts) < len(best[2]):
                    best = (r, c, opts)
    if best is None:
        return True                                   # no empty cell -> solved
    r, c, opts = best
    for v in opts:
        g[r][c] = v
        if solve():
            return True
        g[r][c] = 0                                   # backtrack
    return False

if solve():
    for row in g:
        print(*row)
else:
    print("No solution")
