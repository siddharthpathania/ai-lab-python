# B3 8-Queens backtracking - col[r] = column of queen in row r.
# Safe = no earlier queen in same column or diagonal (|row diff| == |col diff|).
N = 8
col = [0] * N
count = 0

def safe(r, c):
    for i in range(r):                    # every queen already placed (rows above)
        if col[i] == c:                   # same column
            return False
        if abs(col[i] - c) == r - i:      # same diagonal
            return False
    return True

def solve(r):
    global count
    if r == N:
        count += 1
        if count == 1:
            for x in col:
                print(". " * x + "Q " + ". " * (N - x - 1))
        return
    for c in range(N):
        if safe(r, c):
            col[r] = c
            solve(r + 1)          # when this returns, loop tries next column = backtrack

solve(0)
print("Total solutions:", count)
