import sys
from collections import deque

def bfs(v):
    queue = deque([v])
    check[v] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not check[i]:
                queue.append(i)
                check[i] = 1

N, M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
check = [0] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
for i in range(1, N+1):
    if check[i]:
        continue
    bfs(i)
    ans += 1

print(ans)