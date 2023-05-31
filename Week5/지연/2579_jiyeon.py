import sys

answer = 0

N = int(sys.stdin.readline())

arr = list(int(sys.stdin.readline()) for _ in range(N))

dp = [0]*300

if N == 1:
    print(arr[0])
    exit()
if N == 2:
    print(arr[0] + arr[1])
    exit()

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

for i in range(3, N):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1])

print(dp[N-1])