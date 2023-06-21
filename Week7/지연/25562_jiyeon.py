import sys

N = int(sys.stdin.readline())

print(N*(N-1)//2)
print(*list(2**i for i in range(N)))

print(N-1)
print(*list(i for i in range(2, N+2)))