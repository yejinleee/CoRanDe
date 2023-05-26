# 5. 순열사이클 (실3)

import sys
input = sys.stdin.readline

#dfs
def dfs(v):
  visited[v] = 1
  if visited[arr[v]-1] == 0:
    dfs(arr[v]-1)

#입력, dfs 호출
T = int(input())
for i in range(T):
  N = int(input())
  arr = list(map(int, input().split()))

  visited = [0]*(N)
  cnt = 0
  while visited.count(0) > 0:
    dfs(visited.index(0))
    cnt += 1
  print(cnt)
