# 3. 아기 상어(골3)
# 거리, 행, 열 순으로 우선순위 ->힙으로 풀어보자

import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def findShark():
  for i in range(N):
    for j in range(N):
      if arr[i][j] == 9:
        return i, j

def bfs():
  w = 2 #상어 크기
  t = 0 #시간
  cnt = 0
  X, Y = findShark()
  dx = [-1, 0, 0, 1]
  dy = [0, -1, 1, 0]

  while True:
    q = deque()
    q.append((X, Y))
    h = []
    f = 0
    end = 0

    #자신보다 큰 물고기 못 지나감, 지나갈 수 있는 곳만 0으로 바꾸기
    visited = [] 
    for i in range(N):
      v = []
      for j in range(N):
        if arr[i][j] <= w or arr[i][j]==9:
          v.append(0)
        else:
          v.append(1)
      visited.append(v)

    #하나 먹을 때까지 반복문 돌기
    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
          continue
        if visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y]+1
          if h and visited[nx][ny] > h[0][0]:
            end = 1
            break
          q.append((nx, ny))
          if 1<=arr[nx][ny]<w and arr[nx][ny] != 9: # 상어가 9보다 커질 때 예외처리
            heapq.heappush(h, (visited[nx][ny], nx, ny))
            f = 1
      if end == 1:
        break

    #먹은 게 있으면 최소힙 꺼내서 계산    
    if f == 1:
      cnt += 1
      if cnt == w:
        cnt = 0
        w += 1
      dis, rx, ry = h[0]
      t += dis
      arr[X][Y] = 0
      arr[rx][ry] = 9
      X, Y = rx, ry
    else: #먹은게 없다면 계산 종료
      break
  print(t)

bfs()