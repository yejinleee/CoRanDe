# 2. The Game of Death(실4)

import sys
input = sys.stdin.readline

# dfs
def dfs(v, cnt):
  if v == N:
    print(cnt)
    return
  if visited[v]:
    print(0)
    return
  visited[v] = 1
  dfs(A[v-1], cnt+1)
  
# 입력 & dfs 호출
T = int(input())
for i in range(T):
  N = int(input())
  A = [int(input()) for _ in range(N)]
  visited = [0]*(N+1)
  dfs(A[0], 1)
