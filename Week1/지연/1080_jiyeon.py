import sys

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

cnt = 0

def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            change(i, j)
            cnt += 1

if A != B:
    print(-1)
else:
    print(cnt)