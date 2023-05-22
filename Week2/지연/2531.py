import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
S = [int(input()) for _ in range(N)]

result = 0
arr = S[0:K]
K = [0]*(D+1)

for i in range(K):
    K[arr[i]] += 1
K[C] += 1

for i in range(N):
    if (D+1)-K.count(0) > result:
        result = (D+1)-K.count(0)

    K[arr.pop(0)] -= 1
    arr.append(S[(i+K)%N])
    K[S[(i+K)%N]] += 1

print(result)