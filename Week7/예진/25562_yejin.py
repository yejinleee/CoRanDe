# 차의 개수

import sys
input = sys.stdin.readline
from itertools import combinations
n = int(input())

maxli = [1,2]
cmb = [1]
i = 2

while len(maxli) < n:
    maxli.append(maxli[-1] + (maxli[-1] - maxli[0] +2))

c = combinations([i for i in range(1,n+1)],2)
ccnt = []
for ci in c:
    ccnt.append(ci)
print(len(ccnt))
print(' '.join(map(str,maxli)))
print(n-1)
print(' '.join(map(str,[i for i in range(1,n+1)])))

'''
서로다른 차의 갯수 최대 : nC2 서로다른n개중 두개 뽑아서 그 차가 매번 달라야 하니까 .. 풀이보니까 결국 이건 n(n-1) //2였다
최대일때 그 n개의 값들 : 이전값 + (이전값-맨첫값 +2(임의의2임..)) .. 풀이보니까 제곱 ...? 암튼 내건 좋지 않은 풀이같으
서로다른 차의 갯수 최소 : 각각의 차가 다 똑같은 경우이니까 그냥 n-1
최소일때 그 n개의 값들 : 1 ,2,3,4,5 ... 이렇게 1씩커지는 배열

'''