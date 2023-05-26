# 1. 반복수열 (실4)

import sys
input = sys.stdin.readline

A, P = map(int, input().split())

def dfs(v):
  if v in visited:
    print(visited.index(v))
    return
  else:
    visited.append(v)

  v = str(v)
  ans = 0
  for i in v:
    ans += int(i)**P

  dfs(ans)
  

visited = []
dfs(A)