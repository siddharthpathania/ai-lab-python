# A3 A* 8-puzzle - f = g + h (g = moves so far, h = misplaced tiles).
# Always expand the state with smallest f using a heap.
import heapq

goal = "123456780"

def h(board):
    return sum(1 for i in range(9) if board[i] != "0" and board[i] != goal[i])

start = input("Start state, 0 = blank (e.g. 123046758): ")
heap, g, parent = [(h(start), start)], {start: 0}, {start: None}

while heap:
    f, s = heapq.heappop(heap)
    if s == goal:
        break
    r, c = divmod(s.index("0"), 3)
    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= nr < 3 and 0 <= nc < 3:
            t = list(s)
            t[r * 3 + c], t[nr * 3 + nc] = t[nr * 3 + nc], t[r * 3 + c]   # slide tile
            t = "".join(t)
            if t not in g or g[s] + 1 < g[t]:
                g[t], parent[t] = g[s] + 1, s
                heapq.heappush(heap, (g[t] + h(t), t))

if s != goal:
    print("No solution")
else:
    path = []
    while s:
        path.append(s)
        s = parent[s]
    for s in reversed(path):
        print(s[:3], s[3:6], s[6:], "", sep="\n")
    print("Moves:", len(path) - 1)
