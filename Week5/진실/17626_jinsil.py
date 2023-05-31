# 6. Four Squares (실3) PyPy3으로 통과

import sys
import math
input = sys.stdin.readline

n = int(input())

dp = [0]*50001
dp[1] = 1

for i in range(2, n+1):
  mv = 999
  for j in range(1, int(math.sqrt(i))+1):
    mv = min(mv, dp[i-j*j])
  dp[i] = mv+1

print(dp[n])
