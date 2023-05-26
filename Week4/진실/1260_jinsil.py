# 8. DFS와 BFS(실2)

import sys
from collections import deque
input = sys.stdin.readline

#입력, 그래프
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
for i in range(1, N+1):
  graph[i].sort()

#dfs
def dfs(v):
  visited1[v] = 1
  print(v, end=' ')
  for i in graph[v]:
    if visited1[i] == 0:
      dfs(i)

#bfs
def bfs(v):
  q = deque()
  q.append(v)
  visited2[v] = 1
  while q:
    value = q.popleft()
    print(value, end=' ')
    for i in graph[value]:
      if visited2[i] == 0:
        visited2[i] = 1
        q.append(i)

#호출
visited1 = [0]*(N+1)
visited2 = [0]*(N+1)
dfs(V)
print()
bfs(V)

