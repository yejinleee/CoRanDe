# 10. 연결요소의 개수 (실2)

#dfs로 하면 런타임 에러 (RecursionError)뜸

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
  
#bfs
def bfs(v):
	q = deque()
	q.append(v)
	visited[v] = 1
	while q:
		value = q.popleft()
		for i in graph[value]:
			if visited[i] == 0:
				visited[i] = 1
				q.append(i)
  
#bfs 호출
visited = [0]*(N+1)
cnt = 0
for i in range(1, N+1):
	if visited[i] == 0:
		cnt += 1
		bfs(i)

print(cnt)