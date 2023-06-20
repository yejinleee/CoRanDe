# 아기 상어 (골3)

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

''' 문제 조건
자신보다 작음 : 먹을 수 있음. 지나갈 수 있음
자신과 같음 : 지나갈 수 있음
자신보다 큼 : x

먹을수있는게 1보다 많으면
    1) 젤 가까운애
    2) 거리같으면 젤 위쪽애
    3) 거리같고 다 위쪽이면 젤 왼쪽애

자신의 크기만큼의 갯수를 먹어야 크기 +1. 크기가 커지면 먹은 양은 reset
처음 아기상어 크기는 2 !!!
'''

babyshark = 2 # 처음 아기상어의 크기
eat = 0 # 먹은 양
move = 0 # 움직인 횟수(초 수) == 출력값

# 아기상어의 위치(si,sj)를 찾는다
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            si, sj = i,j
            break

dx = [0,-1,1,0]
dy = [-1,0,0,1]

def BFS(x,y):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cango = deque([(x,y)])
    caneat = [] # 먹을 수 있는 물고기들 좌표 리스트
    arr[x][y] = 0
    while cango:
        i,j = cango.popleft()
        for d in range(4):
            ni, nj = i+dy[d], j+dx[d]
            if 0<=ni<n and 0<=nj <n and visited[ni][nj] ==0 : # 현재 아기상어의 위치(x,y)를 기준으로 상하좌우 중 갈수 있는 곳 좌표를 cango에 넣는다.
                if arr[ni][nj] <= babyshark: # 0이거나 자신보다 작거나 같은 물고기가 있어야 갈 수 있다.
                    cango.append((ni,nj))
                    visited[ni][nj] = visited[i][j] +1 #아기상어의 위치에서부터 거리를 셀 수 있다.
                    if 0 < arr[ni][nj] < babyshark:  # 자신보다 작!은! 물고기가 있는 곳이면 caneat에도 넣는다. 맨앞 값은 아기상어 위치로부터 거리
                        caneat.append((visited[ni][nj],ni,nj))

    # return sorted(caneat, key=lambda x : (x[0], x[1],x[2])) # 기준에 따라 정렬하여 return
    return min(caneat) if caneat else ()

while True:
    canEat = BFS(si,sj)
    if not canEat:
        break
    distance , nexti,nextj = canEat # 이제 잡아먹을 물고기까지의 거리, 그 물고기의 i,j위치

    arr[si][sj] = 0
    move+=distance
    eat +=1
    if eat == babyshark:
        babyshark+=1
        eat = 0
    si, sj = nexti,nextj # 그 물고기 위치로 이동
print(move)



''' 문법.

# * deque도 정렬할 수 있다
# q = deque([(1,2),(2,3),(2,1),(1,4)])
# print(q)
# deque([(1, 2), (2, 3), (2, 1), (1, 4)])
# print(sorted(q)) #-> 그냥리스트로 나옴!
# [(1, 2), (1, 4), (2, 1), (2, 3)]

# * 리스트 정렬해서 맨앞값 찾고싶을때 min을 쓸 수 도 있다.
# q = deque([(1,2),(2,3),(2,1),(1,4)])
# print(min(q))
# (1, 2)
'''



### 시간 더 줄이는 방법은 모르겠담 !! visited 처리도 했는데 !!