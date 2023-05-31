import sys
input = sys.stdin.readline

r, c= map(int, input().split())

map = [list(input().rstrip()) for _ in range(r)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
safe = 1
for i in range(r):
    for j in range(c):
        if map[i][j] == 'S':
            for d in range(4):
                if 0<= i+di[d] <r and 0<= j+dj[d] <c:
                    if map[i+di[d]][j+dj[d]] == 'W':
                        safe = 0
                        break
            if safe == 0:
                break
    if safe == 0:
        break

print(safe)
if safe == 1:
    for i in range(r):
        for j in range(c):
            if map[i][j] == 'S':
                for d in range(4):
                    if 0<= i+di[d] <r and 0<= j+dj[d] <c:
                        if map[i+di[d]][j+dj[d]] == '.':
                            map[i+di[d]][j+dj[d]] = 'D'
    for i in range(r):
        for j in range(c):
            print(map[i][j], end= '')
        print('')



## 울타리를 어떻게 설치하는지는 중용하지 않다. 무한히해도 됨 ㅋㅋ