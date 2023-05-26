# 9. 유기농배추 (실2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) #재귀 너무 깊어지면 RecursionError발생

#입력
T = int(input())
for i in range(T):
  M, N, K = map(int, input().split())
  arr = [[0 for _ in range(M)] for _ in range(N)]
  for i in range(K):
    X, Y = map(int, input().split())
    arr[Y][X] = 1

  #dfs
  def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
      return False
    if arr[x][y] == 1: #1이면 dfs를 돌면서 0으로 바꿔줌
      arr[x][y] = 0
      dfs(x-1, y)
      dfs(x, y-1)
      dfs(x+1, y)
      dfs(x, y+1)
      return True
    return False #1이 아니면 바로 False로 탈출

  result = 0
  for i in range(N):
    for j in range(M):
      if dfs(i, j) == True:
        result += 1
  print(result)


