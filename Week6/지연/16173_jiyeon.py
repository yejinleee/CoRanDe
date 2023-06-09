import sys
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft() #인덱스 뽑아서
        if x >= N or y >= N: #범위 넘는지 확인
            continue 
        dx = [0, game[x][y]] #아래랑 오른쪽으로만 움직일 수 있음
        dy = [game[x][y], 0]
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx == x and ny == y) or nx >= N or ny >= N: #0일때 무한루프 돌지 않게하고 범위 넘어가는지 확인
                continue
            if (nx == N-1) and (ny == N-1): #만약 우리가 찾는 좌표에 도달했으면 return
                return 1
            queue.append([nx, ny]) #아니라면 queue에 넣기
    return 0

N = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque()
queue.append([0, 0]) #시작점부터 queue에 넣기

print("HaruHaru") if bfs() else print("Hing")