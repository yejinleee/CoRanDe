import sys
input = sys.stdin.readline

'''
n = 1 2 3 4  5 6  7  8  9
답 = 1 2 3 5 8 13 21 34 55

[n] = [n-1] + [n-2]
'''

n = int(input())
dp = [0,1,2]
for i in range(3, n+1):
    dp.append( dp[i-1] + dp[i-2] )
print(dp[n] % 10007) 
# print(dp[-1]) # n=1 일떄, 2 가 나온다! 예외처리 하거나, [n]