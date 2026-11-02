from collections import deque

grid=[".....",
      ".###.",
      ".##..",
      "...#.",
      "....."]

start, goal=(0,0),(4,4)
parent,q={start:None},deque([start])

while q:
    r,c=q.popleft()
    if(r,c)==goal:
        break
    for nr,nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
        if 0<=nr<5 and 0<=nc<5 and grid[nr][nc]=="." and (nr,nc) not in parent:
            parent[(nr,nc)]=(r,c)
            q.append([nr,nc])

if goal not in parent:
    print("Goal cannot be reached")

else:
    path,p=[],goal
    while p:
        path.append(p)
        p=parent[p]
    print("moves: ",path[::-1])
    print('No. of moves',len(path)-1)        
