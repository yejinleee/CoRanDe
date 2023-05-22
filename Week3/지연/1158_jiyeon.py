import sys

N, K = map(int, sys.stdin.readline().split())

arr = [i for i in range(1, N+1)]
idx = 0

print('<', end='')
for i in range(N):
    if (idx+K-1) < len(arr):
        idx += K-1
    else:
        idx = (idx+K-1) % len(arr)
    if i == N-1:
        print(arr[idx], end='>')
        break
    print(arr[idx], end=', ')
    del arr[idx]