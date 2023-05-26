import sys
from collections import deque

input = sys.stdin.readline

def dfs(graph, v, visited):
    global dfsorder
    dfsorder.append(v)
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    return

def bfs(graph, startv, visited):
    queue = deque([startv]) # deque 선언 초기값은 list등의 iterable 값
    visited[startv] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                bfsorder.append(i)
    return

n, m, startv = map(int, input().split())
dfsorder = []
bfsorder = [startv]

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for g in graph:
    g.sort()

dfs(graph, startv, visited)
print(' '.join(map(str,dfsorder)))

visited = [False] * (n+1)
bfs(graph, startv, visited)
print(' '.join(map(str, bfsorder)))
# print(*bfsorder)
