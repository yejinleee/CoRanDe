# 1. 마법사 상어와 비바라기(골5)

import sys
input = sys.stdin.readline

#입력
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
d = [0]*M
s = [0]*M
for i in range(M):
  d[i], s[i] = map(int, input().split())

#d의 8개 방향
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

#구름 움직이는 함수
def cloud_move(d, s):
  for c in cloud:
    c[0] = (c[0]+ dx[d]*s)%N
    c[1] = (c[1]+ dy[d]*s)%N
    A[c[0]][c[1]] += 1
    visited[c[0]][c[1]] = 1

#대각선 물  
def water_add():
  nx = [-1, -1, 1, 1]
  ny = [-1, 1, -1, 1]
  for c in cloud:
    for j in range(4):
      if 0<=c[0]+nx[j]<N and 0<=c[1]+ny[j]<N:
        if A[c[0]+nx[j]][c[1]+ny[j]]:
          A[c[0]][c[1]] += 1

#새로운 구름 생성
def cloud_new():
  for i in range(N):
    for j in range(N):
      if A[i][j] >= 2 and visited[i][j]==0:
        cloud.append([i, j])
        A[i][j] -= 2

#M개 명령 수행
cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for i in range(M):
  visited = [[0 for _ in range(N)] for _ in range(N)]
  cloud_move(d[i], s[i])
  water_add()
  cloud = []
  cloud_new()

#출력
result = 0
for a in A:
  result += sum(a)
print(result)