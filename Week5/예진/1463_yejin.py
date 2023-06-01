# 1로 만들기

import sys
input = sys.stdin.readline
n = int(input())

dp = [0,0]

for i in range(2,n+1):
    minli = []
    if i%3 ==0:
        minli.append(i//3)
    if i%2==0:
        minli.append(i//2)
    minli.append(i-1)
    dp.append(min(dp[m] for m in minli) +1)
print(dp[-1])

# dp = [0,0,1,1,2,2,]

'''
(나눠떨어진다면) 2로나눈경우 3으로나눈경우 그냥1뺀경우 에서 걸린 횟수 중 최소 +1



4: 2로 나누는거 1 + dp[2]
5: 1을 빼는거 1+dp[4]
6: 3으로 나누는거 1 +dp[2] or 2로나누는거 1+dp[3] 어쨋거나 둘다 최소인 2
7: 1을 빼는거 1+dp[6]
8: 2로 나는거 1+dp[4]
9: 3으로 나눠지는거 1+dp[3]
10 : 2로 나눠지는거 1 + dp[5]
11 : 1빼기 1 + dp[10]
12 : 3으로 나누는거 1 + dp[4] =3    2로나누는거1 + dp[6] =3

'''

