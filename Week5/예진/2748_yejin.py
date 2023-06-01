# 피보나치 2

import sys
input = sys.stdin.readline

n = int(input())
dpt = [0,1]
for i in range(1,n):
    dpt.append(dpt[i]+dpt[i-1])
print(dpt[n])


# 또 새로운 풀이
# a, b = 0, 1
# for i in range(n-1):
#     a,b = b, a+b
# print(b)