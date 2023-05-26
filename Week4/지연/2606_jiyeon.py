import sys

def dfs(v):
    for i in graph[v]:
        if check[i] == 0:
            check[i] = 1
            dfs(i)

N = int(sys.stdin.readline())
T = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
check = [0] * (N+1)

for _ in range(T):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(1)
ans = sum(check)-1

print(ans)