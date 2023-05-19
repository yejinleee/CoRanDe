# 30.쿼드트리 (실1) 맞음

import sys
input = sys.stdin.readline

N = int(input())
Q = [list(map(int, input().rstrip())) for _ in range(N)]

def dfs(x, y, n):
  first = Q[x][y]
  for i in range (x, x+n):
    for j in range (y, y+n):
      if Q[i][j] != first :
        first = -1
        break

  if first == -1:
    print("(", end='')
    dfs(x, y, n//2)
    dfs(x, y+n//2, n//2)
    dfs(x+n//2, y, n//2)
    dfs(x+n//2, y+n//2, n//2)
    print(")", end='')

  else :
    if first == 0:
      print("0", end='')
    else :
      print("1", end='')

  if n == 1:
    return

dfs(0, 0, N)
