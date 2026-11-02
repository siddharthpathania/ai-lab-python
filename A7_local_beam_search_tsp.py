# A7 Local Beam Search TSP - keep best k tours; neighbours = swap 2 cities.
# Each round: all neighbours of all beams -> sort by cost -> keep best k. Stop when no improvement.
import random

d = [[0, 2, 9, 10, 7],
     [2, 0, 6, 4, 3],
     [9, 6, 0, 8, 5],
     [10, 4, 8, 0, 6],
     [7, 3, 5, 6, 0]]
n, k = 5, 3

def cost(t):
    return sum(d[t[i]][t[(i + 1) % n]] for i in range(n))

beams = sorted(([0] + random.sample(range(1, n), n - 1) for _ in range(k)), key=cost)
while True:
    pool = beams[:]
    for t in beams:
        for i in range(1, n):
            for j in range(i + 1, n):
                nb = t[:]
                nb[i], nb[j] = nb[j], nb[i]
                pool.append(nb)
    pool.sort(key=cost)
    if cost(pool[0]) >= cost(beams[0]):
        break
    beams = pool[:k]
    print("Best so far:", beams[0], cost(beams[0]))

print("Final tour:", beams[0] + [0], "cost", cost(beams[0]))
