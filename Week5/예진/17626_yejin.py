# Four Squares ##참고

## DP 이용하면 PyPy3로 제출해야함 .. 

import sys
input = sys.stdin.readline
import math

n = int(input())
sqnum = [i**2 for i in range(1,int(math.sqrt(n))+1)] #제곱수들 모음
dp =[0,1]

for i in range(2,n+1):
    if i in sqnum:
        dp.append(1)
    else:
        dp.append(min(dp[i - sqn] for sqn in sqnum if i-sqn>0) +1 )
print(dp[n])

'''
일단, 15663 = 125^2+ 6^2 + 1^2 + 1^2 이러면 답은 4다.. 1두번이지만 하나로침

제곱수들 모음 sqnum = [1,4,9,16,25,36, . . . .]
어떤 수든 얘네들의 합으로 이뤄질테니까

6을 만든다치면,
dp[5] ,dp[2] 중 최소 +1 번
왜냐? 5를 만든 수에 1^2를 더하면 6이니까. +1번의 의미는 제곱수를 더할테니까 최소갯수인 1개

'''