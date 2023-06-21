import sys
from collections import deque

def bfs():
    while queue:
        s, t, c = queue.popleft()
        if s < t:
            queue.append([s*2, t+3, c+1])
            queue.append([s+1, t, c+1])
        elif s == t:
            print(c)
            break

N = int(sys.stdin.readline())

for i in range(N):
    s, t = map(int, sys.stdin.readline().split())
    queue = deque()
    queue.append([s, t, 0])
    bfs()