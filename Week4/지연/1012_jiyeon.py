import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    graph = [[0 for j in range(M)] for i in range(N)]
    ans = 0
    for i in range(K):
        y, x = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)
