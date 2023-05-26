import sys
input = sys.stdin.readline
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        arr[j][i] = 1 # 방향 반대 주의 ..
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                queue = deque([(i,j)])
                while queue:
                    qi, qj = queue.popleft()
                    for d in range(4):
                        if 0<=qi+di[d]<n and 0<= qj+dj[d] <m :
                            if arr[qi+di[d]][qj+dj[d]] ==1:
                                arr[qi+di[d]][qj+dj[d]] = 0
                                queue.append((qi+di[d], qj+dj[d]))
                cnt +=1
    print(cnt)