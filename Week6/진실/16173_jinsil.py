# 1. 점프왕 쩰리 (Small)(실4)

import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y):
  global f
  if x >= N or y >= N or board[x][y] == 0: #board[x][y] == 0 예외처리 해줘야함
    return
  else:
    if x == N-1 and y == N-1:
      print("HaruHaru")
      f = 1
      return
    dfs(x+board[x][y], y)
    dfs(x, y+board[x][y])

f = 0
dfs(0, 0)
if f == 0:
  print("Hing")