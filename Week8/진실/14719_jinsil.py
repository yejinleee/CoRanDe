# 1. 빗물(골5)

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))

# 그림처럼 배열 만들기
arr = []
for i in range(H, 0, -1):
  a = []
  for j in range(W):
    if height[j] >= i:
      a.append(1)
    else:
      a.append(0)
  arr.append(a)    

# 계산
result = 0
for i in range(H):
  f = 0
  r = 0
  for j in range(W):
    if arr[i][j] == 1: #벽 만나면 그동안 모았던 빗물을 결괏값에 더해주기
      f = 1
      result += r
      r = 0
    if arr[i][j] == 0 and f == 1: #빈 곳인데 벽을 지났으면 빗물 증가
      r += 1
print(result)