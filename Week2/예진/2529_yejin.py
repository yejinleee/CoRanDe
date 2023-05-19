import sys
input = sys.stdin.readline
from itertools import permutations

k = int(input())
sign = list(input().split())

maxp = permutations([i for i in range(9,9-k-1,-1)],k+1)
minp = permutations([i for i in range(0,k+1)], k+1)
maxnum =0
minnum = 9999999999
def check(p):
    for i in range(k):
        if sign[i] == '<':
            if p[i] > p[i+1]:
                return 0
        else: #'>'
            if p[i] < p[i+1]:
                return 0
    return 1
    

for p in maxp:
    if check(p) != 0:
        print(''.join(str(i) for i in p))
        break
for p in minp:
    if check(p) != 0:
        print(''.join(str(i) for i in p))
        break
