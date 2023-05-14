import sys

N, L = map(int, sys.stdin.readline().split())

puddle = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    puddle.append([start, end])
puddle.sort(key = lambda x : (x[0], x[1]))

cnt = 0
curr = 0

for start, end in puddle:
    if start > end:
        continue
    if curr > start:
        start = curr
    
    while True:
        if start >= end:
            break
        start += L
        cnt += 1
    curr = start
print(cnt)