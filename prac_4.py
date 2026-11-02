from collections import deque

def can_move(s,i,to):
    for j in range(i):
        if s[j]==s[i] or s[j]==to:
            return False
    return True

n=int(input("ENTER NUMBER OF DISCS: "))
start, goal= "A"*n,"C"*n
parent={start:None}
q=deque([start])

while q:
    s=q.popleft()
    if s==goal:
        break
    for i in range(n):
      for to in "ABC":
         if to!=s[i] and can_move(s,i,to):
            t=s[:i]+to+s[i+1:]
            if t not in parent:
               parent[t]=(s,f"Disk{i+1}: {s[i]}->{to}")  
               q.append(t)

moves=[]
while parent[s]:
    s,move=parent[s]
    moves.append(move)

for move in reversed(moves):
    print(move)

print("total moves: ",len(moves))




