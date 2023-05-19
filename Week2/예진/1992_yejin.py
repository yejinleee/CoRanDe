import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().rstrip())) for _ in range(n)]

def check(x,y,m):
    if m==1:
        print(li[x][y], end="")
        return
    std = li[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if li[i][j] != std:
                print("(", end="")
                m = m//2
                check(x,y,m)
                check(x,y+m,m)
                check(x+m,y,m)
                check(x+m,y+m,m)
                print(")", end="")
                return
    print(std, end="")

check(0,0,n)
