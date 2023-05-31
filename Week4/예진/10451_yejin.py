## 순열사이클

import sys
input = sys.stdin.readline

t = int(input())

''' union-find 이용 684ms
입력 값을 (i, 값) 형태로 union-find 수행
연결된 사이클 갯수를 셀때는 부모배열을 한번 더 검색해야한다 !!!자식들 중에 연결이 생길 수 있으니까.
'''

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
def union(u,v):
    sp = min(find(parent[u]), find(parent[v]))
    bp = max(find(parent[u]), find(parent[v]))
    parent[bp] = sp

for _ in range(t):
    n = int(input())
    parent = [i for i in range(n+1)]
    li = list(map(int, input().split()))
    for i in range(1, n+1):
        union(i,li[i-1])

    ans = []
    for i in range(1, n+1):
        ans.append(find(parent[i])) #parent배열값으로 find!
    print(len(set(ans)))    #중복값 제거 후 카운트


''' dfs - 532ms
연결 된 싸이클 내 원소 끼리 같은 visited값 가지고 set으로 유니크화 하여 갯수 계산
'''

# def cycleDFS(x, union):
#     visited[x] = union
#     if visited[li[x]] == 0 :
#         cycleDFS(li[x], union)
#     else:
#         return
 
# for _ in range(t):
#     n = int(input())
#     li =[0] + list(map(int, input().split()))
#     # [0, 3, 2, 7, 8, 1, 4, 5, 6]
#     visited = [0] * (n+1)
#     union = 1
#     for i in range(1,n+1):
#         if visited[li[i]] == 0:
#             cycleDFS(li[i], union)
#         union+=1
#     print(len(set(visited)) -1)


''' dfs (ver2) 시간을 조금 단축해보자! - 252ms
DFS함수 따로 선언 없이 메인 안에서 while문으로 재귀이용
'''

# for _ in range(t):
#     n = int(input())
#     li =[0] + list(map(int, input().split()))
#     visited = [0] * (n+1)
#     union = 0
#     for x in li[1:]:
#         if visited[x] == 0:
#             visited[x] = 1
#             next = li[x]
#             while not visited[next]:
#                 visited[next]= 1
#                 next = li[next]
#             union+=1
#     print(union)