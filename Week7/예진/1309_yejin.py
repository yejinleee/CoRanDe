import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0] , dp[1] = 1, 3

for i in range(2,n+1):
    dp[i] = (dp[i-2] + dp[i-1]*2) %9901

print(dp[n]%9901)


'''

0:1
3
7
17

'''

# https://velog.io/@yejinleee/BOJ-1309-%EB%8F%99%EB%AC%BC%EC%9B%90-%ED%8C%8C%EC%9D%B4%EC%8D%AC