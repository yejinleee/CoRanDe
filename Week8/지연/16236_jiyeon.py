import sys
from collections import deque

def bfs():
    visited = [[0 for j in range(N)] for i in range(N)]
    fish = []
    arr[shark[0][0]][shark[0][1]] = 0
    while shark:
        x, y = shark.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not visited[nx][ny]:
                if shark_size >= arr[nx][ny]:
                    shark.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    if (arr[nx][ny] > 0) and (arr[nx][ny] < shark_size):
                        fish.append([nx, ny, visited[nx][ny]])
    fish = sorted(fish, key = lambda x: (x[2], x[0], x[1]))
    if len(fish) == 0:
        return -1
    else:
        return fish

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if li[j] == 9:
            baby_shark = [i, j]
    arr.append(li)

shark = deque()
shark.append(baby_shark)
shark_size = 2
dx = [1, -1, 0, 0]
dy = [0 ,0 ,1, -1]

ans = 0
eat = 0
while True:
    fish = bfs()
    if fish == -1:
        break
    else:
        shark.append([fish[0][0], fish[0][1]])
        ans += fish[0][2]
        eat += 1
        if eat == shark_size:
            eat = 0
            shark_size += 1
print(ans)