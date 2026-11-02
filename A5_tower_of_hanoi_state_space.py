# A5 Tower of Hanoi by state space search (BFS).
# State "AAA": s[i] = peg of disk i (disk 0 = smallest). Goal "CCC".
# A disk can move only if no smaller disk is on its peg or on the target peg.
from collections import deque

def can_move(s, i, to):
    for j in range(i):                    # j = every disk smaller than disk i
        if s[j] == s[i] or s[j] == to:    # smaller disk on my peg or on target peg
            return False
    return True

n = int(input("Disks: "))
start, goal = "A" * n, "C" * n
parent = {start: None}            # parent[state] = (previous state, move made)
q = deque([start])                # queue of states waiting to be checked

while q:
    s = q.popleft()
    if s == goal:
        break
    for i in range(n):            # try every disk
        for to in "ABC":          # try every peg
            if to != s[i] and can_move(s, i, to):
                t = s[:i] + to + s[i + 1:]        # new state: disk i is now on peg "to"
                if t not in parent:
                    parent[t] = (s, f"Disk {i + 1}: {s[i]} -> {to}")
                    q.append(t)

moves = []
while parent[s]:
    s, move = parent[s]
    moves.append(move)
for move in reversed(moves):
    print(move)
print("Total moves:", len(moves))
