maze=[".....",
      "###..",
      "....#",
      "##.##",
      "....."]
goal=(4,4)
visited,path=set(),[]

def dfs(r,c):
    if not (0<=r<5 and 0<=c<5) or maze[r][c]=="#" or (r,c) in visited:
        return False
    visited.add((r,c))
    path.append((r,c))
    if (r,c)==goal:
        return True
    for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
        if dfs(nr,nc):
            return True
    path.pop()
    return False

if dfs(0,0):
    print("Path: ",path)
    print("Moves: ",len(path)-1)

    for r in range(5):
        row=""
        for c in range(5):
            if(r,c) in path:
                row+="* "
            else:
                row+=maze[r][c]+" "
        print(row)

else:
    print("no path")

