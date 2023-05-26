import sys
input = sys.stdin.readline

n = int(input())
pair = int(input())

li = [[] for _ in range(n+1)]
for _ in range(pair):
    l, r = map(int, input().split())
    li[l].append(r)
    li[r].append(l)     #! 그래프 만들 때, 양방향인지 확인하자

infected = [False] * (n+1)

def infectDFS(x):
    for l in li[x]:
        if infected[l] ==False:
            infected[l] = True
            infectDFS(l)

infectDFS(1)
infected[1] = False     #! 1번을 통해 걸린 컴퓨터의 수이니 1은 제외!

print(sum(infected))    # True(감염됨)값의 갯수 합산
