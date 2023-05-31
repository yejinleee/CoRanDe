# 10. 계단 오르기 (실3)

import sys
input = sys.stdin.readline

N = int(input())
step = [int(input()) for _ in range(N)]

dp = [[0 for _ in range(2)] for _ in range(301)]
dp[1][0] = step[0]
dp[1][1] = step[0]

for i in range(2, N+1):
  dp[i][0] = max(dp[i-2]) + step[i-1] #i-2(o), i-1(x)
  dp[i][1] = dp[i-1][0] + step[i-1] #i-2(x), i-1(o)

print(max(dp[N]))
