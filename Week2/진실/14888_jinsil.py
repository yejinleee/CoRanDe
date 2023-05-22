# 32. 연산자 끼워넣기 (실1)

import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

#연산 함수
result = []
def operator(ans, n):
  if n == N:
    result.append(ans)
    return
  for i in range(4):
    if O[i] > 0 :
      O[i] -= 1
      if i == 0:
        operator(ans + A[n], n+1)
      if i == 1:
        operator(ans - A[n], n+1)
      if i == 2:
        operator(ans * A[n], n+1)
      if i == 3:
        operator(int(ans / A[n]), n+1)
      O[i] += 1
  
operator(A[0], 1) 

# 출력
print(max(result))
print(min(result))