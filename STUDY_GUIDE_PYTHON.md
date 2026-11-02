# AI Practical – Python Study Guide

Every program in this folder is short and tested. Run any one with:
```bash
python3 B1_bfs_robot_path.py
```

---

## 0. Python tools you need (learn these first)

| Tool | What it does | Used in |
|---|---|---|
| `from collections import deque` → `q.append(x)`, `q.popleft()` | **Queue** (first in, first out) | BFS: B1, A5 |
| a plain list → `st.append(x)`, `st.pop()` | **Stack** (last in, first out) | A2, B6 |
| `import heapq` → `heappush(h, (f, s))`, `heappop(h)` | **Priority queue**: always gives the smallest `f` | A3 |
| `set()` → `visited.add(x)`, `x in visited` | Remembers what you've already seen | A2, B2 |
| dict `parent = {start: None}` | Remembers where each state came from | A3, A5, B1 |
| `a, b = b, a` | Swap two values | A3, A7 |
| `all(condition for i in range(n))` | True only if the condition holds for every `i` | A5, A6, B3 |
| `for ... else:` | The `else` runs only if the loop did **not** `break` | A2 |
| `global count` | Lets a function change a variable defined outside it | B3 |

### Two tricks that appear again and again

**1. Neighbours of a grid cell (A2, A3, B1):**
```python
for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:   # up, down, left, right
    if 0 <= nr < 5 and 0 <= nc < 5:      # stays inside the grid
```

**2. Rebuilding the path from the goal (A3, A5, B1):**
```python
path, p = [], goal
while p:                   # stop when we reach None (the start's parent)
    path.append(p)
    p = parent[p]
print(path[::-1])          # reverse it: start -> goal
```

### The 5 patterns that cover all 14 programs
| Pattern | One-line idea | Programs |
|---|---|---|
| BFS | Queue, so explore nearest first → shortest path | B1, A5 |
| DFS / Backtracking | Try a choice, go deeper, undo it if stuck | B2, B3, A6, A2 |
| A\* | Heap, always expand the smallest `f = g + h` | A3 |
| Minimax / Alpha-beta | My turn = max, opponent's turn = min | B7, A4 |
| Rules | if / elif on the input | A1, B4, B5 |

---

# PART A

## A1. Vacuum Cleaner – Simple Reflex Agent (15 lines)
**Idea:** The agent sees only `[room, dirty?]` and follows 3 rules. It has no memory.
```python
while dirty["A"] or dirty["B"]:
    if dirty[loc]:      SUCK, dirty[loc] = 0
    elif loc == "A":    MOVE RIGHT, loc = "B"
    else:               MOVE LEFT,  loc = "A"
```
- `dirty` is a dict: `{"A": 1, "B": 0}`, where 1 = dirty.
- The loop stops when both rooms are clean.

**Viva:**
- *Simple reflex agent?* It acts only on the current percept, using condition → action rules.
- *PEAS?* Performance = clean rooms, Environment = rooms A and B, Actuators = wheels and suction, Sensors = location and dirt sensor.
- *Weakness?* It has no memory, so it can loop forever.

## A2. Model-Based Agent – Grid (25 lines)
**Idea:** Like a reflex agent, **plus memory** (internal state):
- `visited` (set) = cells I've already been to
- `path` (list used as a stack) = how I got here

```python
for each neighbour:
    if inside grid and "." and not visited:  move there, add to visited and path, break
else:                       # no neighbour worked
    path.pop()              # go back one step
    pos = path[-1]
```
- `grid` is a list of strings: `"."` = free, `"#"` = wall.
- The `for ... else` runs `else` only when no move was found → **backtrack**.

**Viva:**
- *Reflex vs model-based?* A model-based agent remembers the world (visited cells), so it doesn't loop.
- *What is the internal state here?* The `visited` set and the `path` stack.

## A3. A\* – 8 Puzzle (36 lines)
**Idea:** The board is a string, `"123046758"`, where `0` is the blank. The goal is `"123456780"`.
**f = g + h**: `g` = moves so far, `h` = number of misplaced tiles. Always expand the smallest `f`.
```python
heap = [(h(start), start)]
while heap:
    f, s = heapq.heappop(heap)                 # smallest f
    if s == goal: break
    r, c = divmod(s.index("0"), 3)             # row and column of the blank
    for each neighbour (nr, nc):
        swap blank with that tile -> new string t
        if t is new or cheaper:  g[t] = g[s] + 1, parent[t] = s, push (g[t] + h(t), t)
```
- `divmod(5, 3)` = `(1, 2)`, so index 5 is row 1, column 2.
- Position in the string = `row * 3 + col`.
- If the heap runs out without reaching the goal → "No solution".

**Viva:**
- *Why is A\* optimal?* Because `h` is **admissible**: it never overestimates. Each misplaced tile needs at least 1 move.
- *A better h?* Manhattan distance.
- *Unsolvable example?* `123456870`. If the number of inversions is odd, it can't be solved.

## A4. Alpha-Beta Pruning (21 lines)
**Idea:** Minimax, but it skips branches that can't change the answer.
- `alpha` = best MAX has found so far (starts at −999)
- `beta` = best MIN has found so far (starts at +999)
- MAX updates alpha, MIN updates beta. **If `alpha >= beta` → break (prune).**

```python
if depth == 3: return leaves[i]               # leaf
for child in (2*i, 2*i + 1):                  # binary tree: children of node i
    v = alphabeta(depth + 1, child, not is_max, alpha, beta)
    update best and alpha (MAX) or beta (MIN)
    if alpha >= beta: break
```
Leaves `[3, 5, 6, 9, 1, 2, 0, -1]` → answer **5**, with 2 prunes.

**Viva:**
- *Does it change the answer?* No, it gives the same result as minimax, just faster.
- *Best case?* O(b^(d/2)) instead of O(b^d).

## A5. Tower of Hanoi – State Space Search (27 lines)
**Idea:** We don't use the recursive formula. We **search**.
- **State:** `"AAA"`, where `s[i]` = the peg of disk `i` (disk 0 = smallest). **Goal:** `"CCC"`.
- **Legal move:** disk `i` can go to peg `to` only if **no smaller disk** is on its current peg or on `to`:
  `all(s[j] not in (s[i], to) for j in range(i))`
- Run BFS from the start. Store `parent[t] = (s, "Disk 1: A -> C")` so we can print the moves.

3 disks → **7 moves** (2ⁿ − 1). BFS guarantees this is the minimum.

**Viva:**
- *State space size?* 3ⁿ (each disk can be on any of 3 pegs).
- *Recursion vs state space?* Recursion already knows the trick. Search finds the solution without being told the trick, and the same method works for other problems.

## A6. Sudoku – Backtracking + Constraint Propagation (35 lines)
**`ok(r, c, v)`:** `v` is not in the row, the column, or the 3×3 box.
- Box top-left corner = `(r // 3 * 3, c // 3 * 3)`.
- `i // 3, i % 3` turns `i = 0..8` into the 9 cells of the box.

**`solve()`:**
1. For every empty cell, make `opts` = the list of allowed values.
   - `opts` empty → `return False` (**dead end, found early = constraint propagation**).
   - Remember the cell with the **fewest** options (**MRV**).
2. No empty cell → solved, `return True`.
3. Try each option: `g[r][c] = v` → `solve()` → if it fails, `g[r][c] = 0` (**backtrack**).

**Viva:**
- *As a CSP?* Variables = 81 cells, domain = 1–9, constraints = row, column and box are all different.
- *MRV?* Fill the most constrained cell first, so there are fewer wrong guesses.

## A7. Local Beam Search – TSP (30 lines)
**Idea:** Keep **k = 3** tours at the same time.
```python
beams = 3 random tours (city 0 always first)
loop:
    pool = beams + every "swap two cities" neighbour of every beam
    sort pool by cost
    if the best isn't better than before: stop
    beams = best 3
```
- `cost(t)` = sum of `d[t[i]][t[(i+1) % n]]`. The `% n` makes the tour return to the start.
- `random.sample(range(1, n), n - 1)` = a random order of cities 1..4.
- The answer is cost **26**, which is optimal (checked by brute force).

**Viva:**
- *Beam vs hill climbing?* Hill climbing keeps 1 state, beam search keeps k. Beams share information, because the best ones fill the pool.
- *Problem?* Local optimum: all beams can crowd into the same spot. Stochastic beam search helps with this.

---

# PART B

## B1. BFS – Robot Path (29 lines)
**Idea:** A queue explores everything 1 step away, then 2 steps, and so on. The first time it reaches the goal = shortest path.
```python
parent, q = {start: None}, deque([start])
while q:
    r, c = q.popleft()
    if (r, c) == goal: break
    for each neighbour that is inside the grid, ".", and not in parent:
        parent[neighbour] = (r, c)
        q.append(neighbour)
```
- `parent` is also the visited set: if a cell is in `parent`, it has been seen.
- Then rebuild the path with the trick from section 0.

**Viva:**
- *Complete? Optimal?* Yes and yes, when all steps cost the same.
- *Time?* O(rows × cols).
- *BFS vs DFS?* BFS uses a queue, finds the shortest path, and uses more memory. DFS uses a stack (recursion), uses less memory, and its path isn't always shortest.

## B2. DFS – Maze Solver (29 lines) ← your lab's version
**Idea:** Pick one direction and keep going **deep**. At a dead end, **go back one step (backtrack)** and try another direction.
```python
def dfs(r, c):
    if outside, or "#", or already visited: return False
    add (r, c) to visited and path
    if (r, c) == goal: return True
    for each neighbour (right, down, left, up):
        if dfs(neighbour): return True     # found the goal down this road
    path.pop()                             # dead end -> remove me from the path
    return False
```
- The function **calls itself** for each neighbour. That's recursion, and it acts as the DFS **stack**.
- `path.pop()` is the **backtrack**: this cell led nowhere, so take it off the path.
- At the end, the path is drawn with `*`.

**DFS vs BFS (B1), the most likely viva question:**
| | BFS | DFS |
|---|---|---|
| Uses | Queue | Stack / recursion |
| Explores | Nearest cells first, level by level | One road as deep as possible |
| Shortest path? | ✅ Always | ❌ Not guaranteed |
| Memory | More | Less |

## B2 (other option). DFS – Water Jug (19 lines)
**State:** `(x, y)` = litres in each jug. **6 moves:**
```python
p, q = min(x, b - y), min(y, a - x)    # how much can be poured X->Y and Y->X
[(a, y), (x, b), (0, y), (x, 0), (x - p, y + p), (x + q, y - q)]
#  fill X  fill Y  empty X empty Y  pour X->Y       pour Y->X
```
**dfs(x, y):** already visited → False. Add to `visited` and `path`. Goal → True. Try all 6 moves (recursion). If none works → `path.pop()` (**backtrack**) → False.

Input `4 3 2` → `(0,0) (4,0) (4,3) (0,3) (3,0) (3,3) (4,2)`.

**Viva:**
- *When is it solvable?* When the target is a multiple of gcd(a, b) and target ≤ the bigger jug.

## B3. 8-Queens – Backtracking (24 lines)
`col[r]` = the column of the queen in row `r`. There is one queen per row, so no row check is needed.
```python
def safe(r, c):
    return all(col[i] != c and abs(col[i] - c) != r - i for i in range(r))
#              same column?       same diagonal?
def solve(r):
    if r == 8: count += 1; return
    for c in range(8):
        if safe(r, c):
            col[r] = c
            solve(r + 1)      # when this returns, the loop tries the next column = backtrack
```
Answer: **92 solutions**.

**Viva:**
- *Diagonal rule?* Two queens share a diagonal when |row difference| == |column difference|.
- *Why `global count`?* The function changes a variable that lives outside it.

## B4. Rule-Based Chatbot (23 lines)
- Make the input lowercase, then check rules in order and use the **first** keyword that matches.
- `rules` is a dict: `{"hello": "Hi there!", ...}`. Loop over it with `if key in text`.
- **Pattern capture:** `text.split("my name is")[1]` = everything after the phrase. It's saved in `name` and used later for "what is my name".
- No match → default reply. `"bye"` → `break`.

**Viva:**
- *Limitation?* It only matches keywords and doesn't understand meaning, so rule order matters. A famous example of this kind of chatbot is ELIZA (1966).

## B5. Number Guessing Agent (15 lines)
Binary search over `low = 1, high = 100`:
```python
guess = (low + high) // 2
H -> low = guess + 1      L -> high = guess - 1      C -> done
```
It needs at most **7** guesses, because each answer halves the range (log₂ 100 ≈ 6.6).

**Viva:**
- *What kind of agent?* Goal-based: it uses feedback (percepts) to update its belief, which is the range.

## B6. Goal Stack Planning – Blocks World (49 lines)
**World:** `on = {"A": "T", "B": "A", ...}` = what each block sits on. `"T"` = table, `"H"` = in the hand. `hand` = the block being held, or `None`.

**Every goal or action is a tuple of 3:** `("ON", "C", "A")`, `("CLEAR", "A", None)`, `("STACK", "C", "A")`.

| Function | Job |
|---|---|
| `holds(t, x, y)` | Is this goal true right now? |
| `achieve(t, x, y)` | Which action makes this goal true? |
| `pre(a, x, y)` | Which conditions must be true before doing action `a`? |

| Action | Preconditions |
|---|---|
| STACK(X,Y) | HOLDING X, CLEAR Y |
| UNSTACK(X,Y) | ON X Y, ARMEMPTY, CLEAR X |
| PICKUP(X) | ONTABLE X, ARMEMPTY, CLEAR X |
| PUTDOWN(X) | HOLDING X |

**Main loop – pop the top item:**
1. **Action** and all its preconditions are true → do it (update `on` and `hand`) and print it.
2. **Goal is false** → push the action that achieves it, then push that action's preconditions on top.
3. **Goal is already true** → just drop it.

When the stack is empty, re-check all goals and push back any that became false.

Output: `UNSTACK B A`, `STACK B D`, `PICKUP C`, `STACK C A`.

**Viva:**
- *Sussman anomaly?* Start: C on A; goal: A on B and B on C. Achieving one goal undoes the other, so the plan becomes long and wasteful. This shows that linear goal stack planning isn't optimal.
- *Why a stack?* The newest subgoal must be solved first (LIFO).

## B7. Minimax – Tic-Tac-Toe (44 lines)
The board is `b = [" "] * 9`, cells 0–8. The user types 1–9.
```python
def minimax(is_max):
    if someone won: return +1 (O) or -1 (X)
    if board full:  return 0
    for each empty cell:
        place O (if is_max) or X
        scores.append(minimax(not is_max))
        undo the move
    return max(scores) if is_max else min(scores)
```
`best_move()`: try O in every empty cell, call `minimax(False)` (it's X's turn next), and keep the highest score.

**Viva:**
- *Why undo the move?* We are only trying moves in imagination. The real board must stay the same.
- *Can you beat it?* No. The best you can get is a draw.
- *Speed-up?* Alpha-beta pruning (A4).

---

## Common viva questions
- **Agent** = something that perceives through sensors and acts through actuators. **Rational agent** = it acts to maximise its performance measure.
- **Agent types:** simple reflex → model-based → goal-based → utility-based → learning.
- **Uninformed search** (BFS, DFS) uses no heuristic. **Informed search** (A\*) uses `h(n)`.
- **Admissible heuristic** = it never overestimates the real cost.
- **Local search** (hill climbing, beam) keeps only the current state(s), so it uses little memory, but it can get stuck in a local optimum.
- **CSP** = variables + domains + constraints (Sudoku, N-Queens).

## How to practise (remaining time)
1. Read section 0 (10 minutes).
2. Write B1, B3 and B2 **from memory**. They contain BFS, backtracking and DFS, which make up half the list.
3. Then B7 → A4 (A4 is B7 plus alpha and beta).
4. Then A3 and A5 (both are "BFS with extras").
5. Easy ones last: A1, B4, B5, A2.
6. B6 is the longest. Understand the 3 rules of the loop and the operator table, then write it once.

**Exam tip:** write the comment at the top of each program first (the logic). Even if the code has a bug, the examiner can see you know the algorithm.
