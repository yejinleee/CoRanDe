import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cloud = deque(([N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]))
cross = [[-1, -1], [1, -1], [-1, 1], [1, 1]]

for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    direction = [[0, -s], [-s, -s], [-s, 0], [-s, s], [0, s], [s, s], [s, 0], [s, -s]] 
    x, y = direction[d-1]
    visited = [[0 for i in range(N)] for j in range(N)]
    move = deque()
    while cloud:
        i, j = cloud.popleft()
        if i+x < 0:
            currentx = (N + (i+x)) % N
        elif i+x >= N:
            currentx = (i+x - N) % N
        else:
            currentx = (i+x) % N
        if j+y < 0:
            currenty = (N + (j+y)) % N
        elif j+y >= N:
            currenty = (j+y - N) % N
        else:
            currenty = (j+y) % N
        move.append([currentx, currenty])
        visited[currentx][currenty] = 1
        arr[currentx][currenty] += 1
    while move:
        currentx, currenty = move.popleft()
        cnt = 0
        for i in range(4):
            nx = cross[i][0] + currentx
            ny = cross[i][1] + currenty
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if arr[nx][ny] > 0:
                cnt += 1
        arr[currentx][currenty] += cnt
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if arr[i][j] >= 2:
                    cloud.append([i, j])
                    arr[i][j] -= 2
ans = 0
for i in range(N):
    ans += sum(arr[i])
print(ans)