# 점프왕 쩰리

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
flag = 0
def jellyDFS(i,j):
    global flag
    if arr[i][j] == -1:
        flag = 1
        return
    if arr[i][j] != 0 : # 0일때 처리 안하면 j+arr[i][j] = j라 무한루프 주의 !!
        if j+arr[i][j] < n: # 오른쪽으로 값만큼 이동 가능
            jellyDFS(i, j+arr[i][j])
        if i+arr[i][j] < n: #아래로 값만큼 이동 가능
            jellyDFS(i+ arr[i][j], j)

jellyDFS(0,0)
print("HaruHaru" if flag == 1 else "Hing")