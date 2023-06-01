#피보나치 5

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 21
d[0] = 0
d[1] = 1
for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])

## 선언 방식 이렇게도 !
# dp = [0,1]
# for i in range(1,n):
#     dp.append(dp[i]+dp[i-1])