import sys

# def dp(n):
#     global cnt
#     if n == 1:
#         return cnt
#     cnt += 1
#     if n % 3 == 0:
#         dp(n//3)
#     elif n % 2 == 0:
#         dp(n//2)
#     elif (n-1) % 3 == 0:
#         dp(n-1)
#     elif (n-1) % 2 == 0:
#         dp(n-1)
#     else:
#         dp(n-1)
    
# cnt = 0

# dp(N)

N = int(sys.stdin.readline())

d=[0]*(N+1)

for i in range(2,N+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
        
print(d[N])