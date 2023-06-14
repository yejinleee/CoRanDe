# 태권왕

import sys
input = sys.stdin.readline
c = int(input())

def taekwon(s,t,cnt):
    global mincnt
    if s == t:
        mincnt = min(mincnt, cnt)
        return
    if s*2 <= t+3:
        taekwon(s*2, t+3, cnt+1)
    taekwon(s+1, t, cnt+1)
for _ in range(c):
    s, t = map(int,input().split())
    mincnt = 100
    taekwon(s,t,0)
    print(mincnt)

'''
10 20

11 20
22 23
23 23

오 이렇게 세번 !

'''