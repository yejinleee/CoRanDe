import sys

H, W = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, W-1):
    max_left = max(arr[:i]) #i를 기준으로 왼쪽중에 가장 큰 거
    max_right = max(arr[i+1:]) #i를 기준으로 오른쪽중에 가장 큰 거
    if arr[i] < min(max_left, max_right): #둘 중 작은것만큼 고이기 때문에 그것보다 arr이 작아야함
        ans += min(max_left, max_right) - arr[i] #그만큼 고임

print(ans)