# 3. 바이러스(실3)

import sys
input = sys.stdin.readline

#입력
N = int(input())
E = int(input())
array = [list(map(int, input().split())) for _ in range(E)]

#그래프 만들기
graph = [[] for _ in range(N+1)]
for i in range(E):
  graph[array[i][0]].append(array[i][1])
  graph[array[i][1]].append(array[i][0])

#dfs
def dfs(v):
  visited[v] = 1
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

#dfs 호출하기
visited = [0]*(N+1)
dfs(1)
print(visited.count(1)-1)