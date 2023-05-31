import sys
input = sys.stdin.readline

n = int(input())
p, q = map(int,input().split())
m = int(input())

kinship = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    kinship[x].append(y)
    kinship[y].append(x)

visited = [0] * (n+1)
def kinDFS(x):
    for xi in kinship[x]:
        if visited[xi] == 0:
            visited[xi]= visited[x] +1
            if xi == q: # 주어진 사람의 촌수 구했으면 종료
                return
            kinDFS(xi)

kinDFS(p)
print(visited[q] if visited[q]>0 else -1)