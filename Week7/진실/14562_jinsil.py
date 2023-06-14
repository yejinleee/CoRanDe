# 2. 태권왕 (실1)

import sys
from collections import deque
input = sys.stdin.readline

#bfs
def bfs(s, t):
  q = deque()
  q.append((s, t, 0))
  while q:
    s, t, cnt = q.popleft()
    if s == t:
      print(cnt)
      return
    if s < t: # 이 조건 없으면 메모리 초과
      q.append((s+1, t, cnt+1))
      q.append((s*2, t+3, cnt+1))

#입력
C = int(input())
for i in range(C):
  S, T = map(int, input().split())
  if S*2 > T+3:
    print(T-S)
  else:
    bfs(S, T)