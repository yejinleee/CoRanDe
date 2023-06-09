# 11. 부당한 퍼즐(실2) 못풀겠음

import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())
p1 = list(map(int, input().split()))
p2 = deque(list(map(int, input().split())))
p1_rev = copy.deepcopy(p1)
p1_rev.reverse()

def isPuzzle(N):
  global f
  for i in range(N):
    p2.appendleft(p2.pop())
    if p2[0] == p1[0] or p2[-1] == p1[0]: #양끝 원소 먼저 비교 → 시간 초과 해결
      if list(p2) == p1 or list(p2) == p1_rev:
        f = 1
        return

f = 0
isPuzzle(n)
if f == 1:
  print("good puzzle")
else:
  print("bad puzzle")