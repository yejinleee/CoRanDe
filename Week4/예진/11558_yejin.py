import sys
input = sys.stdin.readline

t = int(input())

def DFS(x):
    if visited[pick[x]] == 0:
        visited[pick[x]] = visited[x] +1
        DFS(pick[x])
for _ in range(t):
    n = int(input())
    pick = [0]
    for _ in range(n):
        pick.append(int(input()))
    if n not in pick:   # 주경이가 불리지 않는 경우 제외
        print(0)
        continue
    visited = [0]*(n+1)
    DFS(1)
    print(visited[n] if visited[n] > 0 else 0)


# DFS로 풀자 !
'''풀이
DFS(x): 매개변수 x는 현재 순서 사람의 번호
다음으로 지목할 사람(pick[x])이 지목당한 적 있다면 순환 상태가 되므로 DFS바로 종료 및 0 출력
없다면, 지목할사람의 순서 = 현재순서 +1 visited[pick[x]] = visited[x] +1
'''



''' 시도 1 - 시간초과
t = int(input())
for _ in range(t):
    n = int(input())
    pick = [0]
    for _ in range(n):
        pick.append(int(input()))
    if n not in pick:
        print(0)
        continue
    visited = [0]*(n+1)
    i, k = 1,1 #시작하는 희현이를 1번째로 카운트 해야함.
    while True:
        if pick[i]==n:
            print(k)
            break
        elif pick[i] == i or visited[pick[i]] == 1:
            print(0)
            break
        visited[pick[i]] = 1
        i = pick[i]
        k+=1
'''