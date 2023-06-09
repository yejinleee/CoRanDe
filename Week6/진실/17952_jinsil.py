# 3. 과제는 끝나지 않아!(실3)
# 시간, 메모리 줄일 필요가 있음

import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0
for i in range(N):
  info = list(map(int, input().split()))
  if info[0] == 1:
    stack.append([info[1], info[2]])
  if stack:
    stack[-1][1] -= 1
    if stack[-1][1] == 0:
      result += stack.pop()[0]

print(result)