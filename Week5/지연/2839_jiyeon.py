import sys

N = int(sys.stdin.readline())

cnt = 0
flag = 0
while True:
    if N % 5 == 0:
        cnt += N//5
        break
    N -= 3
    cnt += 1
    if N < 0:
        flag = 1
        break
if flag:
    print(-1)
else:
    print(cnt)