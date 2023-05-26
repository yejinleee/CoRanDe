import sys
from collections import deque

def dfs(v):
    print(v, end= ' ')
    for i in graph[v]:
        if check[i] == 0:
            check[i] = 1
            dfs(i)

def bfs(v):
    queue = deque([v])
    check[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not check[i]:
                queue.append(i)
                check[i] = 1
    print()

N, M, V = map(int, sys.stdin.readline().split())
check = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1,N+1):
    graph[i].sort()

check[V] = 1
dfs(V)
print()
check = [0] * (N+1)
bfs(V)

