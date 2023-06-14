# 1. 차의 개수 (실3)

import sys
input = sys.stdin.readline

N = int(input())

print(N*(N-1)//2)
for i in range(N):
  print(2**i, end=' ')
print()
print(N-1)
for i in range(N):
  print(i+1, end=' ')