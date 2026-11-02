# B7 Tic-Tac-Toe Minimax - computer O maximises, you X minimise. O win +1, X win -1, draw 0.
b = [" "] * 9
WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def winner():
    for x, y, z in WINS:
        if b[x] == b[y] == b[z] != " ":
            return b[x]

def minimax(is_max):
    w = winner()
    if w:
        return 1 if w == "O" else -1
    if " " not in b:
        return 0
    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if is_max else "X"      # try move
            scores.append(minimax(not is_max))
            b[i] = " "                         # undo move
    return max(scores) if is_max else min(scores)

def best_move():
    best, move = -2, None
    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = minimax(False)
            b[i] = " "
            if score > best:
                best, move = score, i
    return move

while not winner() and " " in b:
    i = int(input("Your move (1-9): ")) - 1
    if b[i] != " ":
        continue
    b[i] = "X"
    if not winner() and " " in b:
        b[best_move()] = "O"
    for r in (0, 3, 6):
        print("|".join(b[r:r + 3]))
print("Winner:", winner() or "Draw")
