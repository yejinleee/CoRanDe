import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000) #재귀횟수 제한 늘려야함

# # # # # DFS 로 풀기. sys.setrecursionlimit(1000000)해야 통과
'''
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
#[[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

def ccDFS(visited, i):
    visited[i] = True
    for v in arr[i]:
        if not visited[v]:
            ccDFS(visited, v)
cnt =0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        ccDFS(visited, i)
        cnt+=1
print(cnt)
'''


### union-find로 풀기


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    sp = min(find(parent[x]), find(parent[y]))  # ^^find..
    bp = max(find(parent[x]), find(parent[y]))
    parent[bp] = sp

for _ in range(m):
    u, v = map(int, input().split())
    union(u,v)

ans = []
for i in range(1, n+1):
    ans.append(find(parent[i])) #parent배열값으로 find!

print(len(set(ans)))    #중복값 제거 후 카운트