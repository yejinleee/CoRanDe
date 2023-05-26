# 4. 촌수계산(실3)

import sys
input = sys.stdin.readline

#입력
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
person = [list(map(int, input().split())) for _ in range(m)]

#그래프 만들기
graph = [[] for _ in range(n+1)]
for i in range(m):
  graph[person[i][0]].append(person[i][1])
  graph[person[i][1]].append(person[i][0])

#dfs
def dfs(v, cnt):
  visited[v] = 1

  if v == p2:
    print(cnt)
    return

  for i in graph[v]:
    if visited[i] == 0:
      dfs(i, cnt+1)
  

#dfs 호출
visited = [0]*(n+1)
dfs(p1, 0)
if visited[p2] == 0:
  print(-1)