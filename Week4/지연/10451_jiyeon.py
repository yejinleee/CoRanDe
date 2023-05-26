import sys

def dfs(v):
    visited[v] = True
    i = graph[v]
    if not visited[i]:
        dfs(i)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    graph = [0] + list(map(int,sys.stdin.readline().split()))
    visited = [False] * (N+1)
    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)