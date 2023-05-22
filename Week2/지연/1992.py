def check(x, y, N):
    if N == 1:
        print(QuadTree[x][y], end='')
        return
    num = QuadTree[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if num != QuadTree[i][j]:
                print("(", end='')
                N //= 2
                check(x, y, N)
                check(x, y+N, N)
                check(x+N, y, N)
                check(x+N, y+N, N)
                print(")", end='')
                return
    print(QuadTree[x][y], end='')
    return

import sys

N = int(sys.stdin.readline())

QuadTree = []
for _ in range(N):
    num = sys.stdin.readline().strip()
    QuadTree.append([int(a) for a in str(num)])

check(0,0,N)