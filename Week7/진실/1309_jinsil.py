# 2. 동물원(실1)

N = int(input())

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 3

for i in range(2, N+1):
  dp[i] = (dp[i-2] + dp[i-1]*2)%9901

print(dp[N]%9901)