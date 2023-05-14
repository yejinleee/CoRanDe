import sys

N = int(sys.stdin.readline())

for _ in range(N):
    d = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))

    sum = 0
    smax = 0
    for i in range(d-1, -1, -1):
        if smax > stock[i]:
            sum += smax - stock[i]
        elif smax < stock[i]:
            smax = stock[i]
    print(sum)