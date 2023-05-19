# 29.부등호 (실1) 맞음

import sys
from itertools import permutations
input = sys.stdin.readline

k = int(input())
sign = list(map(str, input().split()))

num = [i for i in range(10)]

result = []
for per in list(permutations(num, k+1)):
  f = 0
  for i in range (k) :
    if sign[i] == '<' and per[i] > per[i+1]:
      f = 1
      break
    if sign[i] == '>' and per[i] < per[i+1]:
      f = 1
      break
  if f == 0:
    result.append(''.join(map(str, per)))
    
print(max(result))
print(min(result))