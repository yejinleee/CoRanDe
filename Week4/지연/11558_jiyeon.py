import sys

def dfs(v):
    for i in graph[v]:
        if check[i] == 0:
            check[i] = check[v]+1
            dfs(i)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    check = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        A = int(sys.stdin.readline())
        graph[i].append(A)
    print(graph)
    dfs(1)
    print(check)
    ans = 0 if check[N] <= 0 else check[N]
    print(ans)