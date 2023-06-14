# 마법사 상어와 비바라기

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
directions = [
    [0,-1], [-1, -1], [-1, 0], [-1,1], [0,1],[1,1],[1,0],[1,-1]
]
diagnol = [
    [-1,-1], [-1, 1], [1,-1], [1,1]
]


def copyWater(i,j):
    global arr
    cnt = 0
    for di in diagnol:
        if 0<=i+di[0]<n and 0<=j+di[1]<n:
            if arr[i+di[0]][j+di[1]] >0:
                cnt += 1
    arr[i][j] += cnt

cloud = deque([[n-1,0], [n-1,1],[n-2,0],[n-2,1]])
for _ in range(m):
    d, s = map(int, input().split())
    move = [directions[d-1][0]*s , directions[d-1][1]*s]
    for _ in range(len(cloud)):
        cl = cloud.popleft()
        cloud.append([(x+y)%n for x,y in zip(cl, move)])
    for c in cloud:
        arr[c[0]][c[1]] +=1
    for _ in range(len(cloud)):
        cl = cloud.popleft()
        copyWater(cl[0],cl[1])
        arr[cl[0]][cl[1]] += 1000
        cloud.append(cl)
    l = len(cloud)
    for i in range(n):
        for j in range(n):
            if 2<= arr[i][j] < 1000:
                arr[i][j] -=2
                cloud.append([i,j])
    for _ in range(l):
        cl = cloud.popleft()
        arr[cl[0]][cl[1]] -= 1000
    
tot = 0
for x in arr:
    tot+=sum(x)
print(tot)


'''파이썬 배열 요소 각각의 합 구하기
a = [1,2]
b= [3,4]
print([x+y for x,y in zip(a,b)])
'''


'''1차 완성

def copyWater(i,j):
    global arr
    cnt = 0
    for di in diagnol:
        if 0<=i+di[0]<n and 0<=j+di[1]<n:
            if arr[i+di[0]][j+di[1]] >0:
                cnt += 1
    arr[i][j] += cnt

cloud = [[n-1,0], [n-1,1],[n-2,0],[n-2,1]]
for _ in range(m):
    d, s = map(int, input().split())
    # print(cloud, '시작cloud')
    move = directions[d-1]
    for _ in range(s):
        for i in range(len(cloud)):
            cloud[i] = [(x+y)%n for x,y in zip(cloud[i],move)]
    # print(cloud, '완성cloud') # [[4, 2], [4, 3], [3, 2], [3, 3]]
    for c in cloud:
        arr[c[0]][c[1]] +=1
    ## 구름있던 칸에 1씩 증가까지 완.
    # print(arr, '2. 구름있던칸 물 +1')
    newcloud = []
    for i in range(n):
        for j in range(n):
            if [i,j] in cloud:
                copyWater(i,j)
    for i in range(n):
        for j in range(n):
            if [i,j] not in cloud:
                if arr[i][j] >=2 :
                    arr[i][j] -=2
                    newcloud.append([i,j])
    # print(arr, '4&5')
    # print(newcloud)
    cloud = newcloud
tot = 0
for x in arr:
    tot+=sum(x)
print(tot)


무조건 시간초과 나올것 같음 ^^
'''

'''2차 - deque도입


'''