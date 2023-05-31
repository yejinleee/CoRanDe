# 3. 다리놓기(실5)

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N, M = map(int, input().split())
	dp = [1]*(M+1)
	for i in range(1, M+1):
		dp[i] *= dp[i-1]*i
	print(dp[M]//(dp[M-N]*dp[N]))

