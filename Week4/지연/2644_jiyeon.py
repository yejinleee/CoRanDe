import sys

def dfs(v):
    for i in graph[v]:
        if check[i] == 0:
            check[i] = check[v]+1
            dfs(i)

n = int(sys.stdin.readline())
x1, x2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

check = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(x1)
print(graph)
print(check)
ans = -1 if check[x2] <= 0 else check[x2]

print(ans)