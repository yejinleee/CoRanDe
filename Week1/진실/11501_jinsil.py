# 20. 주식(실2) 맞음

import sys
input = sys.stdin.readline

T = int(input())
N = []
S = []
answer = []

for i in range (T) :
  N = int(input())
  S = list(map(int, input().split()))

  m = S[N-1]
  result = 0
  for j in range (N-1, -1, -1) :
    if S[j] < m :
      result += m-S[j]
    else :
      m = S[j]
  
  answer.append(result)

for i in range(T) :
  print(answer[i])
