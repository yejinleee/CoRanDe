import sys

R, C = map(int,sys.stdin.readline().split())

graph = [sys.stdin.readline().strip() for _ in range(R)]

dx = [0, 1, 0 ,-1]
dy = [-1, 0 , 1, 0]
flag = 1

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'W':
            for k in range(4):
                x, y = dx[k], dy[k]
                if (x+i) < 0 or (x+i) >= R or (y+j) < 0 or (y+j) >= C:
                    continue
                if graph[x+i][y+j] == 'S':
                    print(0)
                    flag = 0

if flag:
    print(1)
    for i in range(R):  
        print(graph[i].replace('.', 'D'))
