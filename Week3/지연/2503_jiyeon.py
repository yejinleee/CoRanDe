import sys
from itertools import permutations

N = int(sys.stdin.readline())

baseball = []

for _ in range(N):
    baseball.append(list(map(int, sys.stdin.readline().split())))

num = [i for i in range(1, 10)]

P = list(permutations(num, 3))

answer = 0

for ballnum in P:
    flag = True
    for q, s, b in baseball:
        sc = 0
        bc = 0
        q = str(q)
        if str(ballnum[0]) == q[0]:
            sc += 1
        if str(ballnum[1]) == q[1]:
            sc += 1
        if str(ballnum[2]) == q[2]:
            sc += 1
        if (str(ballnum[0]) == q[1]) or (str(ballnum[0]) == q[2]):
            bc += 1
        if (str(ballnum[1]) == q[0]) or (str(ballnum[1]) == q[2]):
            bc += 1
        if (str(ballnum[2]) == q[0]) or (str(ballnum[2]) == q[1]):
            bc += 1
        if (s != sc) or (b != bc):
            flag = False
            break
    if flag:
        answer += 1

print(answer)