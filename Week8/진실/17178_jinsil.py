# 1. 줄서기(골5)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().rstrip().split())) for _ in range(N)]
for i in range(N):
  for j in range(5):
    a = arr[i][j].split('-')
    a[1] = a[1].zfill(3) #4를 004로 바꾸기 위해
    arr[i][j] = a[0]+a[1]

stack = []
result = []

f = 0
for i in range(N):
  for j in range(5):
    if len(stack) == 0 or stack[-1] > arr[i][j]:
      stack.append(arr[i][j])
    else:
      while True:
        result.append(stack.pop())
        if len(stack) == 0 or stack[-1] > arr[i][j]:
          break
      stack.append(arr[i][j])
      if len(result) > 1 and result[-1] < result[-2]:
        f = 1
        break

if stack: #스택에 남아있는 것들도 다 result에 넣어주기
  while stack:
    result.append(stack.pop())
    if len(result) > 1 and result[-1] < result[-2]:
      f = 1
      break

if f == 0:
  print("GOOD")
else:
  print("BAD")