# 다리놓기

import sys
sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    re = 1
    for i in range(m,m-n,-1):
        re *= i
    for i in range(n,1,-1):
        re = re//i
    print(re)